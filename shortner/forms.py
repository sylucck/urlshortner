from django import forms
from .models import ShortenerModel, ProfileModel

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#form for long_url
class ShortenerForm(forms.ModelForm):
    
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "form-control form-control-lg", "placeholder": "Your URL to shorten"}))
    
    class Meta:
        model = ShortenerModel

        fields = ('long_url',)


#form for ProfileModel

#creating a Registration Form
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
