from django.db import models
from django.core import validators

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year = models.IntegerField(validators=[validators.MinValueValidator(1960)])
    cost = models.IntegerField(validators=[validators.MinValueValidator(0)])

    def __str__(self):
        return self.name


    
