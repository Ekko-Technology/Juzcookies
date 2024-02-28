from django.contrib import admin
from .models import Order, OrderedItems

# Register your models here.
admin.site.register(Order)

# make certain columns in django admin readonly
class OrderedItemsAdmin(admin.ModelAdmin):
    readonly_fields = ('date_ordered','items_ordered', 'total_price')  # Fields that are always readonly

admin.site.register(OrderedItems, OrderedItemsAdmin)
