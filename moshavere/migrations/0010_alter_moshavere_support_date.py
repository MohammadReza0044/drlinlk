# Generated by Django 4.0.6 on 2022-08-03 09:06

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('moshavere', '0009_alter_moshavere_support_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moshavere',
            name='support_date',
            field=django_jalali.db.models.jDateField(),
        ),
    ]