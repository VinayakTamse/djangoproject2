from django.contrib import admin
from django.urls import path
from restapiemployee import views


urlpatterns = [
   
   path('employee/', views.employee_lists_create.as_view()),
   path('employee/<int:pk>/', views.employee_ret_up_del.as_view()),
   
]