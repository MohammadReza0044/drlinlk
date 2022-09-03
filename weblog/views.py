from django.db.models import Count
import math
from django.shortcuts import render 
from django.shortcuts import get_object_or_404 , get_list_or_404
from django.core.paginator import Paginator
from django.views import View
from datetime import datetime , timedelta
from django.contrib import messages



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
    # most_visit_obj=Posts.objects.all().order_by('-post_visit')[0:10]
    most_visit_obj = Visitors.objects.filter(page__contains="blog/").order_by('visit_time')[0:10]
    print (most_visit_obj)


    relative_posts = Posts.objects.filter(category_id = posts.category_id).order_by('-post_date')[0:10]
    datestring = posts.post_date
    modify = posts.post_modified
    dt = datetime.fromtimestamp(float(datestring))
    mt = datetime.fromtimestamp(float(modify))
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
    return render(request, 'weblog/article.html', {'posts': posts, 'comment': comment, 'dt':dt, 'mt':mt, 'relative_posts':relative_posts,'most_visit_obj':most_visit_obj})
        
                                         

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


def tags_detail(request,pk):
    tag_detail = PostTags.objects.filter(tag_id = pk)
    posts = PostTags.objects.filter(id__in=tag_detail)

   
    result = Posts.objects.filter(id = posts)


    return render(request, 'weblog/tags_detail.html', {'result': result})