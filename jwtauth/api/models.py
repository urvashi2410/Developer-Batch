from django.db import models

# Create your models here.
class Todo(models.Model):
    heading = models.CharField(max_length=50)
    isDone = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.heading