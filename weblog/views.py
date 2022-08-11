import math
from django.shortcuts import render 
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.views import View
from django.http import HttpResponseRedirect



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


def post_detail(request,pk):
    posts = get_object_or_404 (Posts, pk=pk)
    if request.method == 'POST':
       author_sender = request.POST ['author'] 
       author_email_sender = request.POST ['author_email'] 
       comment_content_sender = request.POST ['comment_content'] 

       new_comment = Comments.objects.create(post=posts , author=author_sender, author_email=author_email_sender, comment_content=comment_content_sender)
    return render(request, 'weblog/article.html', {'posts': posts})
    
        


                                                   
    

def search (request):
    if request.method == 'GET':
        q = request.GET.get('search')
    post_list = Posts.objects.filter(post_title_fa__icontains = q)
    return render (request, 'weblog/blog.html' , {'post_list':post_list})


# def comment_submit (request, pk):
#     if request.method == 'POST':
#        author_sender = request.POST ['author'] 
#        author_email_sender = request.POST ['author_email'] 
#        comment_content_sender = request.POST ['comment_content'] 

#        new_comment = Comments(post=pk , author=author_sender, author_email=author_email_sender, comment_content=comment_content_sender)
#        new_comment.save()
#        return render (request,'weblog/article.html')



