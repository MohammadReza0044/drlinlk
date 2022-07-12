from django.urls import path

from .views import survery_submit

urlpatterns = [
    path('', survery_submit),
]
