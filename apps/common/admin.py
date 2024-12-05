from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(UserLocation)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ProductImage)
admin.site.register(Category)
