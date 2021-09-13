from django.contrib import admin
from django.urls import path
from api import views


urlpatterns = [
   path('employees/', views.display_all_employee_data),
   path('employee/<slug:id>/', views.display_single_employee),
   path('create_employee/', views.create_employee_data),
   path('update_employee/<int:id>/', views.update_employee_data),
   
   
]