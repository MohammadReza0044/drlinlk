from django.db.models import Count
import math
from datetime import datetime
from django.shortcuts import render 
from django.shortcuts import get_object_or_404 , get_list_or_404
from django.core.paginator import Paginator
from django.views import View
import datetime
from django.contrib import messages
from collections import Counter
from django.utils import timezone



from jalali_date import datetime2jalali, date2jalali


from .models import Posts , post_Comments , Visitors , PostTags , Tags
from .forms import comment_form




def post_view(request):
    posts= Posts.objects.all().order_by('-post_date')
    paginator = Paginator(posts, 9) # Show 9 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'weblog/blog.html',  {'page_obj': page_obj})


def post_detail(request,post_name):
    posts = get_object_or_404(Posts,post_name=post_name)
    posts.post_visit +=1
    posts.save()
    
    first_date = datetime.datetime.now() - datetime.timedelta(30)
    most = Visitors.objects.filter(visit_time__date = first_date)
    most_list_pages = []
    for p in most:
        most_page = p.page
        most_list_pages.append (most_page)

    blog_pages = [word for word in most_list_pages if 'blog/' in word]
    post_name= []
    for item in blog_pages:
        if item.startswith ('/blog/'):
            item.split('/')
            x = item.replace("/blog/", "", 1)
            y = x.replace("/", "", 1)
            post_name.append(y)

    most_visited = Posts.objects.filter(post_name__in = post_name)[0:10]
   
    relative_posts = Posts.objects.filter(category_id = posts.category_id).order_by('-post_date')[0:10]
    datestring = posts.post_date
    modify = posts.post_modified
    dt = datetime.datetime.fromtimestamp(float(datestring))
    mt = datetime.datetime.fromtimestamp(float(modify))
    if request.method == 'POST':
        form = comment_form(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author'] 
            author_email = form.cleaned_data ['author_email'] 
            comment_content = form.cleaned_data ['comment_content'] 
            form.save(commit=False)
            new_comment = post_Comments.objects.create(post=posts , author=author, author_email=author_email, comment_content=comment_content)
            messages.add_message(request, messages.SUCCESS, 'دیدگاه شما با موفقیت ثبت شد')
    comment = post_Comments.objects.filter (post=posts, status='approved')
    return render(request, 'weblog/article.html', {'posts': posts, 'comment': comment, 'dt':dt, 'mt':mt, 'relative_posts':relative_posts,'most_visited':most_visited})
        
                                         

def search (request):
    if request.method == 'GET':
        query = request.GET.get('search')
    post_result = Posts.objects.filter(media_description__icontains = query)
    
    
    return render (request, 'weblog/search.html' , {'post_result':post_result, 'query':query})





def my_view(request):
	jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')



def tags_view(request):
    tags = Tags.objects.all()
    return render(request, 'weblog/tags.html', {'tags': tags})


def tags_detail(request,name_clean):
    tag_detail = Tags.objects.filter(name_clean = name_clean)
    posts = PostTags.objects.filter(tag_id__in=tag_detail)

    post_id_list = []
    result = []
    for id in posts:
        post_id = id.post_id
        post_id_list.append (post_id)

    for r in Posts.objects.filter(id__in = post_id_list):
        result.append(r)
    
    return render(request, 'weblog/tags_detail.html' , {'result': result})