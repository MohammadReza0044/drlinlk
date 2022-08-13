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
    posts = (get_object_or_404 (Posts, post_name=post_name))
    if request.method == 'POST':
        form = comment_form(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author'] 
            author_email = form.cleaned_data ['author_email'] 
            comment_content = form.cleaned_data ['comment_content'] 
            form.save(commit=False)
            new_comment = Comments.objects.create(post=posts , author=author, author_email=author_email, comment_content=comment_content)
    comment = Comments.objects.filter (post=posts, status='approved')
    return render(request, 'weblog/article.html', {'posts': posts, 'comment': comment})
    
        
                                         

def search (request):
    if request.method == 'GET':
        query = request.GET.get('search')
    post_result = Posts.objects.filter(media_description__icontains = query)
    return render (request, 'weblog/search.html' , {'post_result':post_result, 'query':query})


from jalali_date import datetime2jalali, date2jalali

def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')



