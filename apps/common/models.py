from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    SELLER = 'seller'
    User = 'user'

    ROLE_CHOICES = [
        (SELLER, 'Seller'),
        (User, 'User'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=User,
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # related_name qo'shildi
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # related_name qo'shildi
        blank=True,
    )

    def __str__(self):
        return self.username

class User(models.Model):
    pass 

class Seller(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'yangi'
        MODERATION = 'Moderation', 'Moderatsiya'
        COD_VERIFIED = "cod_verified", 'kod tasdiqlangan'

    full_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    birth_date = models.DateField()
    register_certificate = models.FileField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    expired_date = models.DateTimeField()
    code = models.CharField(max_length=250)
    status = models.CharField(
        max_length=50, 
        choices=Status.choices, 
        default=Status.NEW
    )

    def __str__(self):
        return self.full_name
    
class UserLocation(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Order(models.Model):
    class DeliveryType(models.TextChoices):
        MARKET = 'market', "do'kondan"
        HOME = "home", 'uydan'

    class Status(models.TextChoices):
        IN_PROCESS = 'process', "jarayonda"
        PAID = "paid", "to'langan"

    delivery_type = models.CharField(max_length=250, choices=DeliveryType.choices)
    price = models.IntegerField()
    status = models.CharField(max_length=250, choices=Status.choices)

    def __str__(self):
        return str(self.price)

class Category(models.Model):
    name = models.CharField(max_length=250)

class ProductImage(models.Model):
    image1 = models.ImageField()

class Product(models.Model):
    class Status(models.TextChoices):
        IN_PROCESS = 'process', "jarayonda"
        PAID = "paid", "to'langan"
        UNPAID = "unpaid", "to'lanmagan"
        CANCELLED = "cancelled", "bekor qilingan"

    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.PositiveIntegerField()
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=250, choices=Status.choices)
    comment = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    images = models.ManyToManyField(ProductImage)

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    count = models.PositiveIntegerField()

    def __str__(self):
        return str(self.count)
