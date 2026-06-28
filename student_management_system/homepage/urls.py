from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('course/<str:pageName>', views.coursePage, name='coursePage'),
]   