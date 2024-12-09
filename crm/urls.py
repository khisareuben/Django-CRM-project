from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.user_login, name='login'),
  path('register/', views.user_register, name='register'),
  path('user_logout/', views.user_logout, name='logout'),
  path('record/<int:pk>', views.user_record, name='record'),
]
