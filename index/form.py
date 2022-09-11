from django import forms

from weblog.models import Newsletters 

class email_form(forms.ModelForm):
    class Meta:
        model = Newsletters
        fields = ['email']