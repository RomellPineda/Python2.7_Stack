from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.newblog),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)$', views.num),
    url(r'^(?P<number>\d+)/edit$', views.num),
    url(r'^(?P<number>\d+)/delete$', views.dele),
]