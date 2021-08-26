from django import forms
from .models import UserMember, Profile

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

JOB_LOCATIONS = (
    ('Bangalore', 'Bangalore'),
    ('Pune', 'Pune'),
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi')
)

class UsersMemberRegister(forms.ModelForm):

    class Meta:

        model = UserMember
        fields = ['Name', 'Email']
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'})
        }

    
class Agents(forms.Form):

    Agent_Name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}), label='Name')
    Agent_Phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}), label='Phone')


class ProfileForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    Job_city = forms.MultipleChoiceField(choices=JOB_LOCATIONS, widget=forms.CheckboxSelectMultiple)

    class Meta:

        model = Profile
        fields = ['name', 'DOB', 'gender', 'city', 'Pin', 'State', 'Mobile', 'email', 'Job_city', 'profile_img', 'prof_file']
        labels = {'DOB':'Date of Birth', 'Job_city':'Prefered Location', 'profile_img':'Profile Image', 'prof_file':'Upload Document'}
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'DOB': forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'Pin': forms.NumberInput(attrs={'class':'form-control'}),
            'State': forms.Select(attrs={'class':'form-control'}),
            'Mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }
   