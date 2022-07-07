from .models import user_details
from django import forms

class get_user(forms.ModelForm):
    
    class Meta:
        model = user_details
        fields = ['username','email']
