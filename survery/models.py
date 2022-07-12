from django.db import models



class survey(models.Model):
    lessthan30 = "LESS THEN 30"
    between31to35 = "BETWEEN 31 TO 35"
    between36to40 = "BETWEEN 36 TO 40"
    above40 = "ABOVE 40"


    AGE_CHOICES = (
        (lessthan30, "LESS THEN 30"),
        (between31to35, "BETWEEN 31 TO 35"),
        (between36to40, "BETWEEN 36 TO 40"),
        (above40, "ABOVE 40"),
    )


    full_name = models.CharField(max_length= 100)
    age = models.CharField(max_length=50, choices= AGE_CHOICES)
    clinic_name = models.CharField(max_length= 150)
    education =  models.CharField(max_length= 150)
    specialty =  models.CharField(max_length= 150)

    def __str__(self) -> str:
        return f"{self.full_name}"