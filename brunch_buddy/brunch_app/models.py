from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    #location = models.ForeignKey(Neighborhood)
    location = models.CharField(max_length=50)
    status = models.BooleanField()
    #phone = models.
    #rating = models.
    #number_of_reviews = models.
    

