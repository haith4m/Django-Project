from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput



# Creates/ Registers a User(model form)
class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','email','password1','password2']


# Authenticates a User (Model Form)
        
class LoginForm(AuthenticationForm):
     
     username = forms.CharField(widget=TextInput())
     password = forms.CharField(widget=PasswordInput())

 