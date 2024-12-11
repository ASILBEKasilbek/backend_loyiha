from django.db import models

# Create your models here.

class User(models.Model):
    pass 
class Seller(models.Model):


    class Status(models.TextChoices):
        NEW = 'new', 'yangi',
        MODERATION = 'Modeartion', 'Moderatsiya'
        COD_VERIFIED =  "cod_verified", 'kod tasdiqlangan'

    full_name=models.CharField(max_length=250)
    father_name=models.CharField(max_length=250)
    birth_date=models.DateField()
    register_certificate=models.FileField()
    phone=phone = models.CharField(max_length=15, blank=True, null=True)
    expired_date=models.DateTimeField()
    code=models.CharField (max_length=250)
    status= models.CharField (max_length=50, 
    choices=Status.choices, 
    default=Status.NEW
    )

    def __str__(self):
        return self.full_name
    
class UserLocation(models.Model):
        latitude=models.FloatField()
        longitude=models.FloatField()
        user=models.ForeignKey(User, on_delete=models.PROTECT)

class Order(models.Model):
    class Delivery_type(models.TextChoices):
        MARKET = 'market', "do'kondan"
        HOME =  "home", 'uydan'

    class Status(models.TextChoices):
        IN_PROCESS = 'proccess', "djarayonda "
        PAID  =  "paid", "to'langan"

    delivery_type =  models.CharField(max_length=250, choices=Status)
    price=models.IntegerField()
    status=models.Choices(models.CharField(max_length=250, choices=Status))

    def __str__(self):
        return self.price


class Category(models.Model):
    name=models.CharField(max_length=250)

class ProductImage(models.Model):
        image1=models.ImageField()


class Product(models.Model):
     
    class Status(models.TextChoices):
        IN_PROCESS = 'proccess', "jarayonda "
        PAID  =  "paid", "to'langan"
        UNPAID = "unpaid" , "to'lanmagan"
        CANCELLED = "cancelled", "bekor qilingan"
  

    name=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    price=models.DecimalField()
    count=models.PositiveIntegerField()
    description=models.CharField(max_length=250)
    status=models.Choices(status=models.Choices(models.CharField(max_length=250, choices=Status)))
    comment=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    images=models.ManyToManyField()



class OrderItems(models.Model):
        product=models.ForeignKey(Product, on_delete=models.PROTECT)
        order=models.ForeignKey(Order, on_delete=models.PROTECT )
        count=models.PositiveIntegerField()

        def __str__(self):
            return self.count
                                     

