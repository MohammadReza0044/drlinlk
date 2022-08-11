from django.urls import path

from .views import post_view , post_detail , search 

urlpatterns = [
    path('', post_view),
    path('/search/', search , name= "search"),
    path('/<pk>/', post_detail),

    
    
    
    
]


    

