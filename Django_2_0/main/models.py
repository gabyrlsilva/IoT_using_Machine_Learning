from django.db import models

# Create your models here.

class iris(models.Model):
    features = models.CharField(max_length=50)
    label = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.features