from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^send', views.sent),
    url(r'^res', views.result),
]