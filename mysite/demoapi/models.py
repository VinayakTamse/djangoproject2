from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=20)
    emp_salary = models.IntegerField()

class Material(models.Model):
    mat_id = models.AutoField(primary_key=True)
    mat_name = models.CharField(max_length=30)
    mat_price = models.IntegerField()
    
