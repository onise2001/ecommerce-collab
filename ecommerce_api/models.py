from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    inStock = models.IntegerField()


class Order(models.Model):
    total = models.FloatField()
    user = models.ForeignKey(to=('users.CustomUser'), on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.ForeignKey(to=('users.CustomUser'), on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField()

class OrderItem(models.Model):
    product = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

