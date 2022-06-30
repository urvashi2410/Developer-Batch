from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    isGraduated = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.name 