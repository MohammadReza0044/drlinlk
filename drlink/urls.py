"""drlink URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path , include
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap
from weblog.sitemap import PostSitemap , StaticSitemap


sitemaps={
    'posts':PostSitemap,
    'static':StaticSitemap,
    
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('survery', include(('survery.urls' , 'survery') , namespace='survery')),
    path('blog', include(('weblog.urls' , 'weblog') , namespace='weblog')),
    path('contact-us', include('contact_us.urls')),
    path('support', include(('moshavere.urls' , 'support') , namespace='moshavere')),
    path('', include(('index.urls' , 'index') , namespace='index')),
    path('', include(('static_pages.urls', 'static_pages') , namespace='static_pages')),
    path(
        'sitemap.xml',sitemap, {'sitemaps':sitemaps}, name='django.contrib.sitemaps.views.sitemap'
    ),
    
    
]
