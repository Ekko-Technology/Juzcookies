from django.db import models
from bakery.models import Cakes, Pastries
from django.utils import timezone
import pytz
# Create your models here.

class Order(models.Model):
    cake = models.ForeignKey(Cakes, on_delete=models.SET_NULL,null=True, blank=True)
    pastry = models.ForeignKey(Pastries, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    # def __str__(self):
    #     return self.cake


class OrderedItems(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    unit_number = models.CharField(max_length=20)
    items_ordered = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)

    # adjusting datetime to singapore's
    singapore_tz = pytz.timezone("Asia/Singapore")

    def get_singapore_time():
        return timezone.now().astimezone(OrderedItems.singapore_tz)
    
    date_ordered = models.DateTimeField(default=get_singapore_time)

    # confirmation of payment. admin to tock when payment is complete.
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        status = "PAID" if self.complete else "UNPAID"

        return f"{self.first_name}'s order ({self.date_ordered.date()} ) [{status}]"