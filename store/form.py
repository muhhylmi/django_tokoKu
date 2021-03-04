from django.forms import ModelForm
from .models import Customer
from django import forms


class FormCustomer(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

        widgets = {
            "name": forms.TextInput({'class': 'form-control'}),
            "email": forms.TextInput({'class': 'form-control'}),
            "user": forms.Select({'class': 'form-control'}),
        }
