from django import forms
from .models import Calculation
#creating forms

class CalculationForm(forms.ModelForm):
    class Meta: #info related to forms
        model= Calculation
        fields = ['principal','rate','time']

