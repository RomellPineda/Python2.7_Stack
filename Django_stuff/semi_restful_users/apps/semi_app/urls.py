from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^users', views.index),
    url(r'^addnew$', views.new),
    url(r'^create$', views.create),
    url(r'^show/(?P<number>\d+)$', views.show),
    url(r'^edit/(?P<number>\d+)$', views.edit),
    url(r'^update/(?P<number>\d+)$', views.update),
    url(r'^delete/(?P<number>\d+)$', views.delete),
]