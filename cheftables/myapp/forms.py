from django import forms
from django.forms.widgets import NumberInput

class DemoForm(forms.Form):
    name=forms.DateField(label="Reservation Date",widget=NumberInput(attrs={"type" : "date"}))