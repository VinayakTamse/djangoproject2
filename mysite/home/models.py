from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExtraField(models.Model):
    phone_no = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    user =  models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)

    def __str__(self):

        return self.name

class UserMember(models.Model):
    usermemberId = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=20)
    Email = models.CharField(max_length=50)

    def __str__(self):

        return self.Name

class AgentMode(models.Model):
    ag_id = models.AutoField(primary_key=True)
    ag_name = models.CharField(max_length=20)
    ag_phone = models.CharField(max_length=15)


    def __str__(self):
        return self.ag_name



