from django.db import models

# Create your models here.
class Pastries(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='mainpage/aboutuspics')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(blank=True, max_length=50)
    modal_description = models.TextField(blank=True)
    new = models.BooleanField()
    bestseller = models.BooleanField()
    sold_out = models.BooleanField()

    def __str__(self):
        return self.title
    

class Cakes(models.Model):
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to='mainpage/aboutuspics')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(blank=True, max_length=50)
    modal_description = models.TextField(blank=True)
    new = models.BooleanField()
    bestseller = models.BooleanField()
    sold_out = models.BooleanField()

    def __str__(self):
        return self.title
    




    
