from django.urls import path

from .views import about_us, about_product, rules, privacy


urlpatterns = [
    path('about-us', about_us , name='about-us'),
    path('about-product', about_product, name='about-product'),
    path('rules', rules , name='rules'),
    path('privacy', privacy , name='privacy'),
    
    
    
]
