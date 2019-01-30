from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('read', views.read),
    path('update/<id>', views.update),
    path('delete/<id>', views.delete),
]
