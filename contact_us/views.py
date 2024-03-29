from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
import json
from django.contrib import messages

from .models import contact_us
from.forms import contactUs_form
from .api import sessionName

def contactUs_submit(request):
    if request.method == 'POST':
        form = contactUs_form(request.POST)
        if form.is_valid():
           form.save() 
           messages.add_message(request, messages.SUCCESS, 'پیغام شما با موفقیت ثبت شد')
           data = form.cleaned_data
           url = "https://drlink.crm24.io/webservice.php"

           payload={'sessionName': sessionName(),
            'operation': 'create',
            'elementType': 'Leads',
            'element': json.dumps({
                "assigned_user_id": "19x8",
                "lastname":data ['name'],
                "cf_1198":data ['email'],
                "cf_1190":data ['text'],
                "creator":"19x8"
            
                
              })

            }

           files=[

            ]
           headers = {}

           response = requests.request("POST", url, headers=headers, data=payload, files=files)
           

           return render (request,'contact_us/contact-us.html',{'form': form})
    else:
        form = contactUs_form()  
    
    return render (request,'contact_us/contact-us.html',{'form': form})

              

  










    
