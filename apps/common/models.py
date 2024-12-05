from django.db import models

# Create your models here.
class Seller(models.Model):
    full_name=models.CharField(max_length=250)
    father_name=models.CharField(max_length=250)
    birth_date=models.DateField()
    register_certificate=models.FileField()
    phone=models.IntegerField()
    expired_date=models.DateTimeField()
    code=models.CharField(max_length=250)
    # status=models.Choices()
    latitude=models.FloatField()
    longitude=models.FloatField()
    # user=models.ForeignKey()
class UserLocation(models.Model):
    latitude=models.FloatField()
    longitude=models.FloatField()
    # user=models.ForeignKey()
class Order(models.Model):
    price=models.IntegerField()
    # delivery_type=models.Choices()
    # status=models.Choices()

class OrderItems(models.Model):
    # product=models.ForeignKey()
    # order=models.ForeignKey()
    count=models.PositiveIntegerField()
class ProductImage(models.Model):
    image1=models.ImageField()
class Category(models.Model):
    name=models.CharField(max_length=250)
class Product(models.Model):
    name=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    # price=models.DecimalField()
    count=models.PositiveIntegerField()
    description=models.CharField(max_length=250)
    # status=models.Choices(names='4')
    comment=models.TextField()
    # category=models.ForeignKey()
    # images=models.ManyToManyField()
class User(models.Model):
    pass 