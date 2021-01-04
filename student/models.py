from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 60)
    fname = models.CharField(max_length = 60)
    mname = models.CharField(max_length = 60)
    dob = models.DateField()

    def __str__(self):
        return self.name

# Create your models here.
