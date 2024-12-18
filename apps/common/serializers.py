from rest_framework import serializers
from .models import *
import django_filters

class StoreFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')  
    class Meta:
        model=Store
        fields=['name','address']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
class StoreSerializer(serializers.ModelSerializer):
    book_set=BookSerializer(many=True,read_only=True)
    class Meta:
        model=Store
        fields='__all__'

class PhoneNumberSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)

class VerificationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    verification_code = serializers.CharField(max_length=6)
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role'],
        )
        return user



class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model=Seller
        fields='__all__'


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

# class ProductListSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=Product
#         fields='__all__'

# class ProductUpdateSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = models.Product
#             exclude = ("id","created_at")



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