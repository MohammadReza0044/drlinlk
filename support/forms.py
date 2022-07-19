from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget

from .models import support

class support_form(forms.ModelForm):
     class Meta:
        model= support
        fields = ('support_date',)

     def __init__(self, *args, **kwargs):
        super(support_form, self).__init__(*args, **kwargs)
        self.fields['support_date'] = JalaliDateField (label=('support_date'), 
            widget=AdminJalaliDateWidget)