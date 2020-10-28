from django import forms
from .models import iris

class IrisForm(forms.ModelForm):
    class Meta:
        model = iris
        fields = ['features', 'label']