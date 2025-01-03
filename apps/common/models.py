from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

class Store(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='store/images/',blank=True,null=True)
    def __str__(self):
        return self.name


class Book(models.Model):
    TYPE_CHOICES=[
        ('R','Roman'),
        ('Q','Qissa'),
        ('H','Hikoya')
    ]
    store=models.ForeignKey(Store,related_name='books',on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    description=models.TextField()
    author=models.CharField(max_length=250)
    image=models.ImageField(upload_to='store/images/',blank=True,null=True)
    hajmi=models.IntegerField(default=0)
    category=models.CharField(max_length=1,choices=TYPE_CHOICES,default='R')
    turi=models.CharField(max_length=250,default='roman')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.title



class UserPhoneVerification(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    verification_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_number
    

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
        related_name='customuser_set',  
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions', 
        blank=True,
    )

    def __str__(self):
        return self.username

class User(models.Model):
    name=models.CharField(max_length=250, default='Unknown')
    surname=models.CharField(max_length=250, default='Unknown')
    father_name=models.CharField(max_length=250, default='Unknown')
    birth_date = models.DateField(null=True, blank=True)

    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
    
class Seller(models.Model):
    class Status(models.TextChoices):
        NEW = 'new', 'yangi',
        MODERATION = 'Modeartion', 'Moderatsiya'
        COD_VERIFIED =  "cod_verified", 'kod tasdiqlangan'

    full_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250)
    birth_date = models.DateField()
    register_certificate = models.FileField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    expired_date = models.DateTimeField()
    code = models.CharField(max_length=250)
    # status = models.CharField(
    # max_length=50, 
    # choices=Status.choices,default=Status.NEW
    # )

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
   

    price=models.IntegerField()
    status=models.CharField(max_length=250, choices=Status.choices)

    def __str__(self):
        return self.price


class Category(models.Model):
    name = models.CharField(max_length=250)

class ProductImage(models.Model):
    image1 = models.ImageField(upload_to='images/')

class Product(models.Model):
    class Status(models.TextChoices):
        IN_PROCESS = 'process', "jarayonda"
        PAID = "paid", "to'langan"
        UNPAID = "unpaid", "to'lanmagan"
        CANCELLED = "cancelled", "bekor qilingan"
  

    name=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    count=models.PositiveIntegerField()
    description=models.CharField(max_length=250)
    status=models.CharField(max_length=250, choices=Status.choices)
    comment=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    images=models.ManyToManyField(ProductImage)



class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    count = models.PositiveIntegerField()

    def __str__(self):
        return str(self.count)
                                     

