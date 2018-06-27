from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^add$', views.add),
    url(r'^newbook$', views.newbook),
    url(r'^book_info/(?P<number>\d+)$', views.info),
    url(r'^review/(?P<number>\d+)$', views.review),
    url(r'^logout$', views.logout),
]