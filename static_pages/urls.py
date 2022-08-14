from django.urls import path

from .views import about_us, about_product, rules, privacy


urlpatterns = [
    path('about-us', about_us ),
    path('about-product', about_product ),
    path('rules', rules),
    path('privacy', privacy),
    
    
    
]
