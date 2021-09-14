from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api2 import views

router = DefaultRouter()

router.register("employee", views.EmployeeAPI, basename="employee")



urlpatterns = [

    path('', include(router.urls))
   
  
  
   
]