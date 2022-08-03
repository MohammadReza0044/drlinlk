from django.http import JsonResponse
from django.shortcuts import render
import requests
import json



from .forms import supportForm
from .api import sessionName

def support_submit(request):
    if request.method == 'POST':
        form = supportForm(request.POST)
        if form.is_valid():
            form.save()
            data = form.cleaned_data
            url = "https://drlink.crm24.io/webservice.php"

            payload={'sessionName': sessionName(),
            'operation': 'create',
            'elementType': 'Leads',
            'element': json.dumps({
                "assigned_user_id": "19x8",
                "lastname":data ['full_name'],
                "cf_1192":data ['clinic_name'],
                "mobile":data ['phone_number'],
                "cf_1210":data['support_date'],
                "cf_1201":data ['support_time'],
                "creator":"19x8"
            
                
              })
            

            }
            print(payload)
            files=[

            ]
            headers = {}

            response = requests.request("POST", url, headers=headers, data=payload, files=files)
           
         
            return render (request,'moshavere/support.html',{'form': form})
    else:
        form = supportForm()
    
    return render (request,'moshavere/support.html',{'form': form})
      

