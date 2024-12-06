from rest_framework import serializers
from .models import Seller,UserLocation,Order,OrderItems,Product,ProductImage,Category,User

class SellerSerializers(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields='__all__'
class UserLocationSerializers(serializers.ModelSerializer):
    class Meta:
        model=UserLocation
        fields='__all__'
class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'
class OrderItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model=OrderItems
        fields='__all__'
class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
class ProductImageSerializers(serializers.ModelSerializer):
    class Meta:
        model=ProductImage
        fields='__all__'
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'