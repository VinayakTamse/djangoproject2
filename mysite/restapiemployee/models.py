from django.db import models

# Create your models here.

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self):
        return self.name
