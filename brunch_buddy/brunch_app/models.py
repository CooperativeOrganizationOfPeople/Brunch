from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    #location = models.ForeignKey(Neighborhood)
    location = models.CharField(max_length=50)	# defaults to a Neighborhood name, falls back on the City name
    status = models.BooleanField()	# is it 'to-do' or 'done'?
    phone = models.CharField(max_length=20)
    display_phone = models.CharField(max_length=20)
    categories = models.CharField(max_length=200)
    rating = models.IntegerField()
    review_count = models.IntegerField()
    rating_img_url = models.URLField()
    yelp_url = models.URLField()
    yelp_mobile_url = models.URLField()
    