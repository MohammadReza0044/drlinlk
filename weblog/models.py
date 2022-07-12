

# from django.db import models
# from django.db import connections
# from django.contrib.auth.models import User


# class blog (models.Model):
#     category_id = models.IntegerField()
#     comment_count = models.IntegerField()
#     comment_status = models.CharField(max_length=50)
#     media_description = models.CharField(max_length=200)
#     media_name = models.CharField(max_length=200)
#     post_content_fa = models.TextField()
#     post_date = models.DateField()
#     post_modified = models.DateField()
#     post_name = models.CharField(max_length=200)
#     post_status = models.CharField(max_length=50)
#     post_title_fa = models.TextField()
#     post_visit = models.IntegerField()
#     user_id= models.ForeignKey(User, on_delete=models.CASCADE,)
    
#     class Meta:
#         db_table = "posts"

    
#     def __str__(self):
#         return self.post_name