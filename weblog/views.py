from django.shortcuts import render

# from models_new import Posts

def posts_view(request):
    return render(request,'weblog/blog.html')


def post_detail(request, pk):
    pass
