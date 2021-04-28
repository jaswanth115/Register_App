from django.db import models

# Create your models here.
class Student(models.Model):
    
    usn = models.CharField(max_length=10)
    name = models.CharField(max_length=25)
     
    def __str__(self):
        return self.name
