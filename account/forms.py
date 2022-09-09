from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'size': '50'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'size': '50'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'size': '50'}))
    confirm_pass = forms.CharField(label='Confirm',
                                   widget=forms.PasswordInput(attrs={'class': 'form-control', 'size': '50'}))

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username=username).exists()
        if user:
            raise ValidationError('Username already exists...')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('Email already exists...')
        return email

    def clean(self):
        cd = super().clean()
        p1 = cd.get('password')
        p2 = cd.get('confirm_pass')
        if p1 != p2:
            raise ValidationError('Passwords must match!!!')


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username or Email',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'size': '50'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'size': '50'}))


class EditUserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['age', 'bio']
