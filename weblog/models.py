from django.db import models
from jalali_date import date2jalali , datetime2jalali

class Posts(models.Model):
    user_id = models.CharField(max_length=255, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)
    media_name = models.CharField(max_length=255)
    media_description = models.CharField(max_length=255)
    post_date = models.BigIntegerField()
    post_title_fa = models.TextField()
    post_content_fa = models.TextField()
    post_status = models.CharField(max_length=16)
    comment_status = models.CharField(max_length=16)
    post_name = models.CharField(max_length=128)
    comment_count = models.IntegerField()
    post_modified = models.BigIntegerField()
    post_visit = models.IntegerField(blank=True, null=True)

    def get_jalali_date(self):
        return date2jalali (self.post_date)

    class Meta:
        app_label = 'weblog'
        db_table = 'posts'



class post_Comments(models.Model):
    approved = "approved"
    disapproved = "disapproved"
  

    STATUS_CHOICES = (
        (approved, "approved"),
        (disapproved, "disapproved"),
        
    )
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE,)
    author = models.CharField(max_length=127)
    author_email = models.CharField(max_length=64)
    comment_date = models.DateField(auto_now_add=True)
    comment_content = models.TextField()
    status = models.CharField(max_length=20 ,  choices= STATUS_CHOICES , default=disapproved)

    def get_jalali_date(self):
        return date2jalali (self.comment_date)
        


    class Meta:
        ordering = ['-comment_date']
        app_label = 'weblog'
        db_table = 'post_Comments'


class Visitors(models.Model):
    ip = models.CharField(max_length=16)
    visit_time = models.DateTimeField(auto_now_add=True)
    browser = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    page = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    paltform = models.CharField(max_length=255)

    class Meta:
        app_label = 'weblog'
        db_table = 'visitors'


class PostTags(models.Model):
    post_id = models.IntegerField()
    tag_id = models.IntegerField()

    class Meta:
        app_label = 'weblog'
        db_table = 'post_tags'



class Tags(models.Model):
    created_at = models.BigIntegerField()
    name = models.CharField(max_length=255)
    name_clean = models.CharField(unique=True, max_length=255)

    class Meta:
        app_label = 'weblog'
        db_table = 'tags'