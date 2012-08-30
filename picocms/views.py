# -*- encoding: UTF-8 -*-
from django.http import Http404
from django.db.models.loading import get_model
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.admin.views.decorators import staff_member_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.forms.widgets import Select
import models


def detail(request, app, cls, slug):
    """ generic view that return direct CMS model rendered content """
    model = get_model(app, cls)
    if model and issubclass(model, models.CMSModel):
        return model.get_response(request, slug)
    raise Http404


@staff_member_required
def imagechooser(request, app, cls):
    model = get_model(app, cls)
    datas = {
        'tinymce_path': staticfiles_storage.url('tiny_mce'),
        'chosen_path': staticfiles_storage.url('chosen'),
        'admin_path': staticfiles_storage.url('admin')
    }
    if model and issubclass(model, models.CMSModel):
        if getattr(model.CMSMeta, 'image_model', None):
            images = [('', '----')]
            for fileitem in model.CMSMeta.image_model.objects.all().order_by('title'):
                if fileitem.file.name.lower().endswith(('.jpg', '.jpeg', '.gif', '.png')):
                    images.append((fileitem.get_absolute_url(), fileitem.title))
            datas['select_files'] = Select(choices=images, attrs={'class': 'chosen-single', 'style': 'width:200px'}).render('file', '')
            #datas['form_upload'] = None
    # gestion upload if any
    # send result back
    return render(request, 'imagechooser.html', datas)


@staff_member_required
def tinymcejs(request, app, cls):
    datas = {
        'tinymce_path': staticfiles_storage.url('tiny_mce'),
        'imagechooser_path': reverse('picocms-imagechooser', args=(app, cls))
    }
    return render(request, 'tiny_mce_src.js', datas, content_type='application/javascript')
