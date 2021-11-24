from django import forms
from .models import License
from django.core.exceptions import ValidationError


class LicenseCreateForm(forms.Form):

    data = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'data_id'}))
    ipaddress = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'ipaddress_id'}))

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data.get("data")
        if '__' not in cleaned_data:
            raise ValidationError("Data format not correct, missing parts separator")
        else:
            if len(cleaned_data.split('__')) != 3:
                raise ValidationError("Data format not correct, number of parts wrong")
