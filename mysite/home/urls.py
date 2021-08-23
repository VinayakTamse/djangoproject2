from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.registerUser, name='register'),
    path('login/', views.hadleLogin, name='login'),
    path('members/', views.members, name='members'),
    path('delete_member/<int:user_id>/', views.delete_members, name="delete_member"),
    path('update/<str:id>/', views.Update_member, name='update'),
    path('logout/', views.handleLogout, name='logout'),
    path('usermembers/<int:id>', views.user_members_add, name='user_members'),
    path('agent/', views.agents, name="agents"),
    path('search/', views.SearchView.as_view(), name="search"),
   
]