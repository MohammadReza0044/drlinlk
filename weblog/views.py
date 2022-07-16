from django.shortcuts import render 
from django.shortcuts import get_object_or_404


from models import Posts


def post_view(request):
    posts= Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'weblog/blog.html', context=context)


def post_detail(request,pk):
    post= get_object_or_404 (Posts, pk=pk)
    context = {'post': post}
    return render(request, 'weblog/article.html', context=context)
    