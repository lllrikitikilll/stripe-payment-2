from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()


class Order(models.Model):
    order_id = models.IntegerField()
    items = models.ManyToManyField(Item)

