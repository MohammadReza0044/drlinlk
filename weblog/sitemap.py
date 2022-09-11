from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Posts

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    protocol = 'http'
    




    def items(self):
        return Posts.objects.filter(post_status = 'publish')

    
    def location(self,obj):
        return '/blog/%s' % (obj.post_name)
    
 
    # def lastmod(self, obj):
    #     return obj.post_modified



class StaticSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'
    
    def items(self):
        return ['index:homepage_view', 'moshavere:support', 'survery:survery', 'static_pages:about-us' , 'static_pages:about-product', 'static_pages:rules', 'static_pages:privacy']
    def location(self, item):
        return reverse(item)