from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.forms import widgets
from .models import finalEducationChoices

class DateInput(forms.DateInput):
    input_type = 'date'

class EmailInput(forms.EmailInput):
    input_type = 'email'

class SignUpForm(forms.ModelForm):

    username = forms.CharField(label='아이디',max_length=20)
    password1 = forms.CharField(label='비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)
    name = forms.CharField(label='이름', max_length=20)
    birth = forms.DateField(\
        label='생년월일', \
        widget=DateInput)
    gender = forms.ChoiceField(label='성별',choices=(('남성','남성'),('여성','여성')))
    belong = forms.CharField(label='소속',max_length=30)
    position = forms.CharField(label='직위',max_length=20)
    address = forms.CharField(label='주소',max_length=100)
    email = forms.EmailField(label='이메일',widget=EmailInput)
    phone = forms.CharField(label='연락처',max_length=20)
    finalEducation = forms.ChoiceField(label='성별',choices=finalEducationChoices)
    major = forms.CharField(label='전공 및 관심분야',max_length=100)

    class Meta:
        model = CustomUser
        fields = ('username','password1','password2','name','birth','gender','belong','position','address','email','phone','finalEducation','major')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('name','password','birth','gender','is_active','is_superuser')
    
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]