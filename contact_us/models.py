from django.db import models

class contact_us(models.Model):
    name = models.CharField(max_length= 100,blank= False, null= True)
    email = models.EmailField(blank= False, null= True)
    text = models.TextField(blank= False, null= True)


    def __str__(self):
        return self.name
