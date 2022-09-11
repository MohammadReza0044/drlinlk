from django.http import HttpResponseRedirect
from django.shortcuts import render
from datetime import datetime 
from django.contrib import messages

from weblog.models import Posts , Newsletters
from .form import email_form



def blog_list(request):
    form=None
    posts = None
    posts= Posts.objects.all().order_by('-post_date')[0:3]
    if request.method == 'POST':
        form = email_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data ['email'] 
            new_Newsletters = Newsletters.objects.create(email = email)
            messages.add_message(request, messages.SUCCESS, 'ایمیل شما با موفقیت ثبت شد')
            return render (request, 'index/index.html', {'posts': posts})

    
    return render (request, 'index/index.html', {'posts': posts})
