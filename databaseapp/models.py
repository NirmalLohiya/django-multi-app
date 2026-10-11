from django.db import models

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=1000)
    email=models.CharField(max_length=1000)
    dob=models.DateField(max_length=1000)
    def __str__(self):
        return self.name
    


