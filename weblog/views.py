import math
from django.shortcuts import render 
from django.shortcuts import get_object_or_404 , get_list_or_404
from django.core.paginator import Paginator
from django.views import View




from .models import Posts , Comments
from .forms import comment_form


def post_view(request):
    posts= Posts.objects.all()
    paginator = Paginator(posts, 9) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'weblog/blog.html',  {'page_obj': page_obj})


def post_detail(request,post_name):
    posts = get_object_or_404 (Posts, post_name=post_name)
    if request.method == 'POST':
       author_sender = request.POST ['author'] 
       author_email_sender = request.POST ['author_email'] 
       comment_content_sender = request.POST ['comment_content'] 

       new_comment = Comments.objects.create(post=posts , author=author_sender, author_email=author_email_sender, comment_content=comment_content_sender)
    comment = get_list_or_404 (Comments, post=posts)
    return render(request, 'weblog/article.html', {'posts': posts, 'comment': comment})
    
        
                                         

def search (request):
    if request.method == 'GET':
        query = request.GET.get('search')
    post_result = Posts.objects.filter(media_description__icontains = query)
    return render (request, 'weblog/blog.html' , {'post_result':post_result})






