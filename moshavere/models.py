from django.db import models


class moshavere(models.Model):
    between9to12 = "بین ساعت 9 تا 12"
    between16to20 = "بین ساعت 16 تا 20"
 

    TIME_CHOICES = (
        (between9to12,  "بین ساعت 9 تا 12"),
        (between16to20,"بین ساعت 16 تا 20"),
        )
    
    full_name= models.CharField(max_length=100, blank=False)
    clinic_name=models.CharField(max_length=200,  blank=False)
    phone_number=models.IntegerField(blank=False)
    support_date =models.DateField( blank=False)
    support_time =models.CharField(max_length=100, choices=TIME_CHOICES, default=between9to12)


    class Meta:
        app_label = 'moshavere'
        db_table = 'moshavere'  

    def __str__(self):
        return self.full_name
