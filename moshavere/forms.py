from django import forms
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

from .models import moshavere


class supportForm(forms.ModelForm):
    class Meta:
        model = moshavere
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(supportForm, self).__init__(*args, **kwargs)
    #     self.fields['support_date'] = JalaliDateField(label=('support_date'), # date format is  "yyyy-mm-dd"
    #         # widget=AdminJalaliDateWidget # optional, to use default datepicker
    #     )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        