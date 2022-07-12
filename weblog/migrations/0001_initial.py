# Generated by Django 4.0.6 on 2022-07-12 08:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('comment_count', models.IntegerField()),
                ('comment_status', models.CharField(max_length=50)),
                ('media_description', models.CharField(max_length=200)),
                ('media_name', models.CharField(max_length=200)),
                ('post_content_fa', models.TextField()),
                ('post_date', models.DateField()),
                ('post_modified', models.DateField()),
                ('post_name', models.CharField(max_length=200)),
                ('post_status', models.CharField(max_length=50)),
                ('post_title_fa', models.TextField()),
                ('post_visit', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]
