from django.contrib import admin
from django.urls import path
from demoapi import views

urlpatterns = [
    path('employee/', views.Employee_Data),
    path('employee/<slug:id>/', views.Employee_Data),
    path('material/', views.Material_API.as_view()),
    path('material/<int:id>/', views.Material_API.as_view()),
    
   
   
]