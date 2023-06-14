from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="home"),
    path("transform", views.transform, name="tranform"),
]
