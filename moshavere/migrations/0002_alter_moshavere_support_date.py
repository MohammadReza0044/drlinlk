# Generated by Django 4.0.6 on 2022-07-27 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moshavere', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moshavere',
            name='support_date',
            field=models.CharField(max_length=50),
        ),
    ]
