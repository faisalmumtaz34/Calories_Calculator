from attr import field
from django.forms import ModelForm
from .models import Profile, Meal
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class UserForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class AddFood(ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'