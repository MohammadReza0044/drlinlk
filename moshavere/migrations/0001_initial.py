# Generated by Django 4.0.6 on 2022-07-24 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='moshavere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('clinic_name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('support_date', models.DateField()),
                ('support_time', models.CharField(choices=[('بین ساعت 9 تا 12', 'بین ساعت 9 تا 12'), ('بین ساعت 16 تا 20', 'بین ساعت 16 تا 20')], default='بین ساعت 9 تا 12', max_length=100)),
            ],
            options={
                'db_table': 'moshavere',
            },
        ),
    ]
