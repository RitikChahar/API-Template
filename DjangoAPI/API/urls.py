from django.urls import path
from . import views

urlpatterns = [
    path('fullname/', views.fullName),
]