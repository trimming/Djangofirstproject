from django.db import models


# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    login_date = models.DateTimeField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField()
    add_date = models.DateTimeField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
