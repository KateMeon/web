from django.urls import path, re_path
from trips import views

urlpatterns = [
    path('', views.index),
]
