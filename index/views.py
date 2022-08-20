from django.shortcuts import render

from weblog.models import Posts

def blog_list(request):
    posts= Posts.objects.all().order_by('-post_date')[0:3]
    return render (request, 'index/index.html', {'posts': posts})
