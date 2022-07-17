from django.shortcuts import render

from .models import contact_us
from.forms import contactUs_form

def contactUs_submit(request):
    if request.method == 'POST':
        contactusform = contactUs_form(request.POST)
        if contactusform.is_valid():
            name = contactusform.cleaned_data['name'],
            email = contactusform.cleaned_data['email'],
            text = contactusform.cleaned_data['text']
            new_contact = contact_us.objects.create(name = name,
            email = email ,
            text =  text)

            new_contact.save()
            return render (request,'contact_us/contact-us.html',)
    else:
        contactusform = contactUs_form()  
    
    return render (request,'contact_us/contact-us.html',)

              

  



# def contactUs_submit(request):
#    if request.method == 'POST':
#        sender_name = request.POST ['sender_name'] 
#        sender_email = request.POST ['sender_email'] 
#        sender_text = request.POST ['sender_text'] 
    
#        new_contactUs = contact_us (name=sender_name, email=sender_email, text=sender_text)
#        new_contactUs.save()
         
#    return render (request,'contact_us\contact-us.html', {})






    
