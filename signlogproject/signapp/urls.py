from django.urls import path
from signapp import views

urlpatterns = [
    path('', views.log, name="log"),
    path("sign/", views.sign),
]
