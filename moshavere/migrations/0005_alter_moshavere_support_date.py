# Generated by Django 4.0.6 on 2022-08-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moshavere', '0004_alter_moshavere_support_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moshavere',
            name='support_date',
            field=models.IntegerField(max_length=10),
        ),
    ]
