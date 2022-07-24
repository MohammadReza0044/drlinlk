from django.urls import path

from .views import post_view, post_detail

urlpatterns = [
    path('', post_view ),
    path('<int:pk>/', post_detail ),
    
    
]
