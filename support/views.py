from multiprocessing import context
from django.shortcuts import render

from .models import support
from .forms import support_form

from jalali_date import datetime2jalali, date2jalali



def support_submit (request):
    date = None
    supportform = None
    if request.method == 'POST':
        fname = request.POST ['fname'] 
        clinic = request.POST ['clinic']
        phone_number = request.POST ['phone_number']
        # date = request.POST ['date']
        time = request.POST ['time']

        supportform = support_form(request.POST)
        if supportform.is_valid():
            date = supportform.cleaned_data ['date']

        new_support = support(
            full_name = fname,
            clinic_name = clinic,
            phone_number = phone_number,
            support_date = date,
            support_time = time
        )
        new_support.save()
    return render (request,'support\\test.html', {'supportform': supportform})  

    def my_view(request):
	    jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')     