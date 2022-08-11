from django.urls import path

from .views import post_view , post_detail , search 

urlpatterns = [
    path('', post_view),
    path('/search/', search , name= "search"),
    path('/search/', search ),
    path('/<slug:post_name>/', post_detail),
    path('/search/<slug:post_name>/', post_detail),

    
    
    
    
]


    

