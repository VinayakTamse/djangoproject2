from django import forms
from .models import UserMember

class UsersMemberRegister(forms.ModelForm):

    class Meta:

        model = UserMember
        fields = ['Name', 'Email']
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'})
        }

    
class Agents(forms.Form):

    Agent_Name = forms.CharField(max_length=20)
    Agent_Phone = forms.CharField(max_length=50)
   