from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=264)
    color = models.CharField(max_length=264)
    def __str__(self):
        return self.brand
