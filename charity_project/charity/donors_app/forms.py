from django import forms
from django.core import validators
from donors_app.models import Donors

class DonorInfoForm(forms.ModelForm):
    class Meta:
        model = Donors
        fields = '__all__'
