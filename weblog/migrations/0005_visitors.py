# Generated by Django 4.0.6 on 2022-08-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0004_post_comments_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=16)),
                ('visit_time', models.BigIntegerField()),
                ('browser', models.CharField(max_length=255)),
                ('device', models.CharField(max_length=255)),
                ('page', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('paltform', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'visitors',
            },
        ),
    ]
