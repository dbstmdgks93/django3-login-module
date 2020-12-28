from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=20, help_text='input your name')
    birth = forms.CharField(max_length=20, help_text='input your birth')
    gender = forms.CharField(max_length=20, help_text='input your gender')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('name','birth','gender')