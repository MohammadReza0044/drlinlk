import math
from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views import View




from .models import Posts , Comments
from .forms import comment_form


def post_view(request):
    list_count= []
    page = 20
    posts= Posts.objects.all()
    count = posts.count()
    half_count = math.ceil(count/6)
   

    for x in range(half_count):
        list_count.append(x+1)
    
   
    return render(request, 'weblog/blog.html',  {'posts': posts, 'list_count': list_count})


def post_detail(request,post_name):
    posts = get_object_or_404 (Posts, post_name=post_name)
    if request.method == 'POST':
       author_sender = request.POST ['author'] 
       author_email_sender = request.POST ['author_email'] 
       comment_content_sender = request.POST ['comment_content'] 

       new_comment = Comments.objects.create(post=posts , author=author_sender, author_email=author_email_sender, comment_content=comment_content_sender)
    return render(request, 'weblog/article.html', {'posts': posts})
    
        
                                         

def search (request):
    if request.method == 'GET':
        query = request.GET.get('search')
    post_result = Posts.objects.filter(media_description__icontains = query)

    return render (request, 'weblog/blog.html' , {'post_result':post_result})






