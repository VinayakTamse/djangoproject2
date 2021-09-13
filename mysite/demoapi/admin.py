from django.contrib import admin
from demoapi.models import Employee, Material

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['emp_id', 'emp_name', 'emp_salary']

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['mat_id', 'mat_name', 'mat_price']

