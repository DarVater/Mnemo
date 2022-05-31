from django.db import models

class Person(models.Model):
    user_name = models.CharField(max_length=100)
    progress = models.FloatField()
    store = models.TextField()
