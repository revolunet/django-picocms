# -*- encoding: UTF-8 -*-
from django.http import Http404
from django.db.models.loading import get_model
import models


def detail(request, app, cls, slug):
    """ generic view that return direct CMS model rendered content """
    model = get_model(app, cls)
    if model and issubclass(model, models.CMSModel):
        return model.get_response(request, slug)
    raise Http404
