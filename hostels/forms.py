from django.forms import ModelForm 
from .models import Employee

class Employeeform(ModelForm):
    class Meta:
        model=Employee
        fields=['name','age','department','salary']