from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    place = models.CharField(max_length=30)

    def __str__(self):
        return self.name
