# Generated by Django 4.0.6 on 2022-08-03 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moshavere', '0002_alter_moshavere_support_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moshavere',
            name='support_date',
            field=models.DateField(max_length=50),
        ),
    ]
