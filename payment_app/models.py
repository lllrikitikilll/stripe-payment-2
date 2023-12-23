from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name:.7} {self.price}'


class Order(models.Model):
    order_id = models.IntegerField(unique=True)
    items = models.ManyToManyField(Item)




