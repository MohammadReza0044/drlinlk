from django.urls import path

from .views import blog_list

urlpatterns = [
    path('', blog_list),
    
    
    
]
