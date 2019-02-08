from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^addjob$', views.addjob),
    url(r'^view/(?P<number>\d+)$', views.info),
    url(r'^add/(?P<number>\d+)$', views.join),
    url(r'^edit/(?P<number>\d+)$', views.edit),
    url(r'^update/(?P<number>\d+)$', views.update),
    url(r'^delete/(?P<number>\d+)$', views.delete),
    url(r'^process$', views.process),
    url(r'^logout$', views.logout),

]
