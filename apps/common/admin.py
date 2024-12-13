from django.contrib import admin
from .models import *


admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Seller)
admin.site.register(UserLocation)
admin.site.register(Order)
admin.site.register(OrderItems)
admin.site.register(ProductImage)
admin.site.register(Category)
