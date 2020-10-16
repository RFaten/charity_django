from django import forms
from django.core import validators
from donations_app.models import Donations

class DonationInfoForm(forms.ModelForm):
    class Meta:
        model = Donations
        fields = '__all__'
