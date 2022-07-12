from django.urls import path

from .views import posts_view , post_detail

urlpatterns = [
    path('', posts_view),
]
