from django.contrib.auth.models import User
from django import forms
from .models import identity

class resolved_case_details(forms.ModelForm):

    class Meta:
        model = identity
        fields=[
            'cin'
            ]