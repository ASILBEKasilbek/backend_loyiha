from django.contrib import admin
from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('category', 'status','name')
    search_fields = ('category',)
    list_filter = ('category',)


@admin.register(Seller)
class Seller(admin.ModelAdmin):
    list_display = ('full_name', 'father_name','phone')
    search_fields = ('full_name',)
    list_filter = ('full_name', )


@admin.register(UserLocation)
class UserLocation(admin.ModelAdmin):
    list_display = ('latitude','longitude')
    search_fields = ('latitude','longitude',)


@admin.register(Order)
class UserLocation(admin.ModelAdmin):
    list_display = ('price', 'delivery_type')
    search_fields = ('price',)


@admin.register(OrderItems)
class UserLocation(admin.ModelAdmin):
    list_display = ('product', 'count')
    search_fields = ('product',)



admin.site.register(ProductImage)
admin.site.register(Book)
admin.site.register(Store)

@admin.register(Category)
class UserLocation(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)







