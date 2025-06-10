from django.urls import path

from . import views

urlpatterns = [
    path('home', views.Home.as_view()),
    path('authorize', views.Login.as_view())
]