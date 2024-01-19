from app.models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':'This is mandatory field'}
        #for removing the displayed content in html page in using '' in help_texts
        #if u want to give some content we need to give text in value

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']       
