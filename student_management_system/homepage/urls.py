from django.urls import path
# from . import views
from homepage import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('course/<str:courseId>/<str:pageName>', views.coursePage, name='coursePage'),
    path('hello_world/', views.hello_world, name='hello_world'),
    path('scores/',views.scores, name='scores'),
    path('login/', views.loginPage, name='loginPage'),
    path('get_name/', views.getName, name='get_name'),
    path('api/create_course/', views.api_create_course, name='api_create_course'),
]   