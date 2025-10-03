from django import forms
from .models import Reading, Patient

class ReadingForm(forms.ModelForm):
    class Meta:
        model = Reading
        fields = ["reading_type", "value"]

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["name", "age", "email"]
