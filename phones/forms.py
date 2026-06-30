from django import forms
from .models import Smartphone


class SmartphoneForm(forms.ModelForm):
    class Meta:
        model = Smartphone
        exclude = []
        widgets = {
            "created_at": forms.DateInput(attrs={"type": "date"}),
        }

# class ImportarDatos(forms.Form):
