# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Advising(models.Model):
    id = models.IntegerField()
    ip = models.CharField(max_length=32)
    created_at = models.IntegerField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=64)
    time = models.CharField(max_length=5)
    seen = models.IntegerField(blank=True, null=True)
    done = models.IntegerField(blank=True, null=True)

    class Meta:
       app_label = 'weblog'
       db_table = 'advising'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        app_label = 'weblog'
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        app_label = 'weblog'
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        app_label = 'weblog'
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        app_label = 'weblog'
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        app_label = 'weblog'
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        app_label = 'weblog'
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categories(models.Model):
    id = models.IntegerField()
    created_at = models.BigIntegerField()
    name = models.CharField(max_length=255)
    name_clean = models.CharField(max_length=255)

    class Meta:
        app_label = 'weblog'
        db_table = 'categories'


class Comments(models.Model):
    id = models.IntegerField()
    post_id = models.IntegerField()
    comment_author = models.CharField(max_length=127)
    comment_author_email = models.CharField(max_length=64)
    comment_author_ip = models.CharField(max_length=16)
    comment_date = models.BigIntegerField()
    comment_content = models.TextField()
    commpent_approved = models.IntegerField()
    commeent_agent = models.TextField()
    comment_parent_id = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'weblog' 
        db_table = 'comments'


class Customers(models.Model):
    id = models.IntegerField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    national_code = models.CharField(max_length=10)
    mobile = models.CharField(max_length=16)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=255)
    address = models.TextField()
    location_name = models.CharField(max_length=255)
    location_type = models.CharField(max_length=64)

    class Meta:
        app_label = 'weblog'
        db_table = 'customers'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        app_label = 'weblog'
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        app_label = 'weblog'
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        app_label = 'weblog'
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        app_label = 'weblog'
        db_table = 'django_session'


class Files(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255, db_collation='utf8_general_ci', blank=True, null=True)
    type = models.CharField(max_length=255)
    time = models.IntegerField()

    class Meta:
        app_label = 'weblog'
        db_table = 'files'


class Items(models.Model):
    id = models.IntegerField()
    item_name = models.CharField(max_length=255)
    item_description = models.TextField()
    item_price = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'weblog'
        db_table = 'items'


class Messages(models.Model):
    message_id = models.IntegerField()
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=64)
    mobile = models.CharField(max_length=12)
    title = models.CharField(max_length=255)
    messages = models.TextField()
    visitor_ip = models.CharField(max_length=32)
    message_time = models.IntegerField()
    seen = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'weblog'
        db_table = 'messages'


class Newsletters(models.Model):
    id = models.IntegerField()
    email = models.CharField(max_length=255)
    register_time = models.IntegerField()
    user_ip = models.CharField(max_length=64)
    seen = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'weblog'
        db_table = 'newsletters'


class PostTags(models.Model):
    id = models.IntegerField()
    post_id = models.IntegerField()
    tag_id = models.IntegerField()

    class Meta:
        app_label = 'weblog'
        db_table = 'post_tags'


class Posts(models.Model):
    id = models.IntegerField()
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


class Secretaries(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=128)
    mobile = models.CharField(max_length=13)
    clinic_name = models.CharField(max_length=255)
    clinic_phone = models.CharField(max_length=32)
    clinic_address = models.TextField()
    friend_mobile = models.CharField(max_length=13, blank=True, null=True)
    ip = models.CharField(max_length=32)
    created_at = models.IntegerField()
    seen = models.IntegerField()

    class Meta:
        app_label = 'weblog'
        db_table = 'secretaries'


class SurverySurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    clinic_name = models.CharField(max_length=150)
    education = models.CharField(max_length=150)
    specialty = models.CharField(max_length=150)

    class Meta:
        app_label = 'weblog'
        db_table = 'survery_survey'
