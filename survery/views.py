from django.shortcuts import render
from multiprocessing import context
from django.core.exceptions import ValidationError
from django.contrib import messages


from.models import survey




def survery_submit(request):
   if request.method == 'POST':
       name = request.POST ['full_name'] 
       age = request.POST ['age'] 
       clinic = request.POST ['clinic_name'] 
       education = request.POST ['education'] 
       specialty = request.POST ['specialty'] 

       new_survery = survey(full_name=name, age=age, clinic_name=clinic, education=education, specialty=specialty )
       new_survery.save()
       messages.add_message(request, messages.SUCCESS, 'درخواست شما با موفقیت ثبت شد')
        
         
   return render (request,'survery\survery.html')



 


 
   