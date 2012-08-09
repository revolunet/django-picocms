from django.contrib import admin
from django.forms.models import ModelMultipleChoiceField
from mptt.admin import MPTTModelAdmin
import models

#
# Custom CMS admin
#


class CMSModelAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'category', 'position', 'active', 'anonymous_access']
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = ('/static/tiny_mce/tiny_mce.js',
                '/static/js/admin-tinymce.js',
              )
        css = {
            'all': ('/static/css/admin-tinymce.css', )
        }

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        obj.save()

    def get_form(self, request, obj=None, **kwargs):
        form = super(CMSModelAdmin, self).get_form(request, obj, **kwargs)
        if obj and obj.pk:
            # remove self entries in related M2M fields
            for field, field_def in form.base_fields.items():
                if isinstance(field_def, ModelMultipleChoiceField):
                    if getattr(obj, field).model == self.model:
                        form.base_fields[field].queryset = form.base_fields[field].queryset.exclude(pk=obj.pk)

        return form


class CategoryAdmin(MPTTModelAdmin):
    list_display = ['title', 'position']

    def get_form(self, request, obj=None, **kwargs):
        form = super(CategoryAdmin, self).get_form(request, obj, **kwargs)
        if obj and obj.pk:
            form.base_fields['parent'].queryset = form.base_fields['parent'].queryset.exclude(pk=obj.pk)
        return form


admin.site.register(models.CMSCategory, CategoryAdmin)
