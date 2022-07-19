from django.urls import path

from .views import support_submit

urlpatterns = [
    path('', support_submit),
]
