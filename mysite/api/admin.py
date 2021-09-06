from django.contrib import admin
from api.models import Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdminDetails(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'salary']
