from dataclasses import fields
from django import forms

from .models import contact_us

class contactUs_form(forms.ModelForm):

    class Meta:
        model= contact_us
        fields = "__all__"