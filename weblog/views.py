from django.shortcuts import render

from models import Posts


def post_view(request):
    post= Posts.objects.all()

    context = {'post': post}
    return render(request, 'weblog/blog.html', context=context)
