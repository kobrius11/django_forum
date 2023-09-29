from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    """
    Gets POST request data from template, puts into fields passes it to View.
    """
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
    
class LoginUserForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)