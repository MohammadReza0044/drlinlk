from django.urls import path

from .views import contactUs_submit
urlpatterns = [
    path('', contactUs_submit),
    
    
    
]
