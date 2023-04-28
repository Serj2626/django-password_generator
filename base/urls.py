from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home, name='password'),
    path('password/', views.password),
]
