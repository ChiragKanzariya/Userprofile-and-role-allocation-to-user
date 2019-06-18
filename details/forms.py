from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from details.models import ProfileModel


class ProfileForm(ModelForm):
    DESIGNATION_CHOICES = (
        ('P', 'Python'),
        ('NJ', 'Node.js'),
        ('D', 'Designer'),
        ('AN', 'Android'),
        ('I', 'IOS'),
    )

    designation = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple, choices=DESIGNATION_CHOICES)

    class Meta:
        model = ProfileModel
        fields = ('image', 'name', 'role', 'designation', 'other')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
