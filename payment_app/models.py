import stripe
from django.db import models

# Create your models here.


class Item(models.Model):
    CURRENCY = [
        ("EUR", "Euro"),
        ("USD", "United States dollar")
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=3, choices=CURRENCY, default='USD')

    def get_price(self):
        return self.price / 100

    def __str__(self):
        return f'{self.name:.7} {self.price}'


class Order(models.Model):
    order_id = models.IntegerField(unique=True)
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey('Discount', on_delete=models.CASCADE)


class Discount(models.Model):
    title = models.CharField(max_length=255)
    percent_dis = models.IntegerField()
    duration_in_months = models.IntegerField()




