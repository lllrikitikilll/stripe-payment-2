from django.contrib import admin
from django.db.models import Sum

from payment_app.models import Item, Order
# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'order_count', 'order_sum']

    def order_count(self, obj):
        return obj.items.count()

    def order_sum(self, obj):
        return obj.items.aggregate(res=Sum("price"))['res']

