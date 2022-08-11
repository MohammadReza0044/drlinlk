from django.db import models

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

    class Meta:
        app_label = 'weblog'
        db_table = 'posts'



class Comments(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE,)
    author = models.CharField(max_length=127)
    author_email = models.CharField(max_length=64)
    comment_date = models.DateField(auto_now_add=True)
    comment_content = models.TextField()


    class Meta:
        app_label = 'weblog'
        db_table = 'comments'