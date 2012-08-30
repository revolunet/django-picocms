from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'detail/([^/]+)/([^/]+)/([^/]+)$', views.detail, name='picocms-view-detail'),
    url(r'picocms/tinymcejs/([^/]+)/([^/]+)$', views.tinymcejs, name='picocms-tinymcejs'),
    url(r'picocms/imagechooser/([^/]+)/([^/]+)$', views.imagechooser, name='picocms-imagechooser'),
)
