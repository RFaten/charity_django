from django import forms
from django.core import validators
from cases_app.models import Cases

class CaseInfoForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = '__all__'
    
