from django.urls import path

from insql import views

urlpatterns = [
    path("home", views.home),
    path("data", views.data),
]
