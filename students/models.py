from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, null=True)
    student_number = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True)
    program = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name