# Generated by Django 4.2 on 2023-12-23 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_app', '0004_discount_alter_item_currency_order_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='duration_in_months',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]