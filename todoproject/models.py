from django.db import models

# Create your models here.
class Todolist(models.Model):
    Content = models.CharField(max_length=50)
    Publish_date = models.DateTimeField()
