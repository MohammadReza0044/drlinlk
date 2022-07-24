# Generated by Django 4.0.6 on 2022-07-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survery', '0002_alter_survey_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='age',
            field=models.CharField(choices=[('LESS THEN 30', 'LESS THEN 30'), ('BETWEEN 31 TO 35', 'BETWEEN 31 TO 35'), ('BETWEEN 36 TO 40', 'BETWEEN 36 TO 40'), ('ABOVE 40', 'ABOVE 40')], max_length=50),
        ),
    ]