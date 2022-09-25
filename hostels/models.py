#from typing_extensions import Self
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    department=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name
