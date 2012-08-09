from django.conf.urls import patterns, url

import views
urlpatterns = patterns('',
    url(r'detail/([^/]+)/([^/]+)/([^/]+)$', views.detail, name='picocms-view-detail'),
)
