from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CHOICE_FOR_STATE = (
    ('Andhra Pradesh', 'Andhra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu and Kashmir', 'Jammu and Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka', 'Karnataka'),
    ('Kerala', 'Kerala'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Maharashtra', 'Maharashtra'),
    ('Manipur', 'Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab', 'Punjab'),
    ('Rajasthan', 'Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal'),
    ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'),
    ('Daman and Diu','Daman and Diu'),
    ('Delhi', 'Delhi'),
    ('Lakshadweep', 'Lakshadweep'),
    ('Puducherry', 'Puducherry')
)

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

class Profile(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    Pin = models.PositiveIntegerField()
    State = models.CharField(choices=CHOICE_FOR_STATE, max_length=100)
    Mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=100, unique=True)
    Job_city = models.CharField(max_length=100)
    profile_img = models.ImageField(upload_to="static/home/images", blank=True)
    prof_file = models.FileField(upload_to="static/home/doc", blank=True)

    def __str__(self):
        return self.name




