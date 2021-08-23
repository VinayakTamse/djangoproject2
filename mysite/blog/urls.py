from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
   
   path("", views.blog_page, name="blogs"),
   path("blogpost<slug:id>/", views.Detailed_Blog, name="details"),
  
   
]