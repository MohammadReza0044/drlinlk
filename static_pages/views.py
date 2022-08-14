from django.shortcuts import render

def about_us (request):
    return render (request,'static_pages/about-us.html')


def about_product (request):
    return render (request,'static_pages/about-product.html')


def privacy (request):
    return render (request,'static_pages/privacy.html')


def rules (request):
    return render (request,'static_pages/rules.html')