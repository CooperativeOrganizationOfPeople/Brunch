from django.db import models

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)

class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    #location = models.ForeignKey(Neighborhood)
    location = models.CharField(max_length=50)	# defaults to a Neighborhood name, falls back on the City name
    status = models.CharField(max_length=50)	# is it 'to-do' or 'done'?
    phone = models.CharField(max_length=20)
    display_phone = models.CharField(max_length=20)
    categories = models.CharField(max_length=200)
    rating = models.IntegerField(null=True)
    review_count = models.IntegerField(null=True)
    # rating_img_url = models.URLField()
    # yelp_url = models.URLField()
    # yelp_mobile_url = models.URLField()            

    def update(self, name='', location='', status=False, phone='', categories='',rating=0,review_count=0):
        self.name=name
        self.location=location
        self.status=status
        self.phone=phone
        self.categories=categories
        self.rating=rating
        self.review_count=review_count

    
    
