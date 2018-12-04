from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.auth),
    url(r'^login$', views.validate),
    url(r'^signup$', views.register),
    url(r'^signin$', views.login),
    url(r'^home$', views.home),

]