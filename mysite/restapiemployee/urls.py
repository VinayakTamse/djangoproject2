from django.contrib import admin
from django.urls import path, include
from restapiemployee import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('student_api', views.StudentAPI, basename='students')


urlpatterns = [
   
   path('employee/', views.employee_lists_create.as_view()),
   path('employee/<int:pk>/', views.employee_ret_up_del.as_view()),
   path('', include(router.urls)),
   
]