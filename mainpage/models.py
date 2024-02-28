from django.db import models

# Create your models here.
class CoverPic(models.Model):
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to='mainpage/aboutuspics')
    url = models.URLField(blank=False)

    def __str__(self):
        return self.caption

class ReviewPic(models.Model):
    caption = models.CharField(max_length = 50)
    image = models.ImageField(upload_to='mainpage/reviewpics')

    def __str__(self):
        return self.caption