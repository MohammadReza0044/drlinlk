import math
from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views.generic.list import ListView


from models import Posts , Comments


def post_view(request):
    list_count= []
    page = 9
    posts= Posts.objects.all()
    count = posts.count()
    half_count = math.ceil(count/6)
   

    for x in range(half_count):
        list_count.append(x+1)
    
   
    return render(request, 'weblog/blog.html',  {'posts': posts, 'list_count': list_count})


def post_detail(request,pk):
    post = get_object_or_404 (Posts, pk=pk)
    context = {'post': post}
    return render(request, 'weblog/article.html', context=context)
    

