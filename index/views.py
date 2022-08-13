from django.shortcuts import render

from weblog.models import Posts

def blog_list(request):
    posts= Posts.objects.all()[0:6]
    return render (request, 'index/index.html', {'posts': posts})
