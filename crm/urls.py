from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.user_login, name='login'),
  path('register/', views.user_register, name='register'),
  path('user_logout/', views.user_logout, name='logout'),
  path('record/<int:pk>/', views.customer_record, name='record'),
  path('delete_record/<int:pk>/', views.delete_record, name='delete_record'),
  path('add_record/', views.add_record, name='add_record'),
  path('update_record/<int:pk>/', views.update_record, name='update_record'),
]
