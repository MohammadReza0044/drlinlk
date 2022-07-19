from asyncio.windows_events import NULL
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class support (models.Model):
    between15to16 = "بین ساعت 15 تا 16"
    between16to17 = "بین ساعت 16 تا 17"
    between18to20 = "بین ساعت 18 تا 20"
    


    TIME_CHOICES = (
        (between15to16, "بین ساعت 15 تا 16"),
        (between16to17, "بین ساعت 16 تا 17"),
        (between18to20, "بین ساعت 18 تا 20"),
        )
    full_name= models.CharField(max_length=100)
    clinic_name=models.CharField(max_length=200)
    phone_number=models.IntegerField(default=NULL)
    support_date =models.DateField()
    support_time =models.CharField(max_length=100, choices=TIME_CHOICES)


    class Meta:
        app_label = 'support'
        db_table = 'support'  

    def __str__(self):
        return self.full_name