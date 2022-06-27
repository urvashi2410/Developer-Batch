from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    isDone = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.title