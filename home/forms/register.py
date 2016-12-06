from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    """ registration form """

    class Meta:
        model = User

