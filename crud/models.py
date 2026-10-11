from django.db import models

# Create your models here.
#  some create empolyee model  like entit image,name,email,dob,designation,

class Employee(models.Model):
    image=models.ImageField(upload_to='emp_images/',default='')
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=200)
    dob=models.DateField()
    designation=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    


 