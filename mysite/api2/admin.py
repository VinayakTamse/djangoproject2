from django.contrib import admin
from api2.models import Employee

# Register your models here.

@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    list_display = ['id', 'name', 'salary', 'place']
