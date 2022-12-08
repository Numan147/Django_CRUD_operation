from django.db import models

# Create your models here.

class Designation(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=5)
    mobile_number = models.CharField(max_length=10)
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE)