from django.urls import path, include
from generator import views

urlpatterns = [
    path('', views.home),
    path('eggs/', views.eggs),
]
