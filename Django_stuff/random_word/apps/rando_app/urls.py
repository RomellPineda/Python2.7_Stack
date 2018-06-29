from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^generate', views.rando_word),
    url(r'^result', views.result),
]