from django.urls import path
from . import views

from .views import get_courses
from .views import my_view

urlpatterns = [
  path('',views.index,name='index'),
  path('register/', views.register, name='register'),
  path('login/', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('form/',views.form,name='form'),
  path('get_courses/', get_courses, name='get_courses'),
  path('my_view/', my_view, name='my_view'),

]