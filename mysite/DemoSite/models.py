from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

class DemoSite(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    photo = models.ImageField(upload_to='static/DemoSite/images', blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    hobbies = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class DemoUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return "demo_user_"+self.name
