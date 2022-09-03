from django.urls import path

from .views import post_view , post_detail , search , tags_view , tags_detail

urlpatterns = [
    path('', post_view),
    path('/search/', search , name= "search"),
    path('/search/', search ),
    path('/tags/', tags_view ),
    path('/tags/<pk>/', tags_detail ),
    path('/<slug:post_name>/', post_detail),
    path('/search/<slug:post_name>/', post_detail),
    
    
    
    
]


    

