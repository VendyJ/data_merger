from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ["name", "description", "cash_amount"]

class DonateForm(forms.Form):
    amount = forms.DecimalField(label="Částka", max_digits=10, decimal_places=2, min_value=1)