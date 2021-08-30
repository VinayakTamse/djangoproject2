from django.contrib import admin
from django.urls import path
from DemoSite import views


urlpatterns = [

    path('', views.IndexPage.as_view(), name='demosite'),
    path('ajax-crud/', views.CreateOperation, name="ajax-create"),
    path('delete/', views.DeleteOperations, name="delete"),
    path('update/', views.UpdateOperations, name="update"),
    
    
   
]