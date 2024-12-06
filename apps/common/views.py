from django.shortcuts import render,HttpResponse
from .models import Seller,UserLocation,Order,OrderItems,Product,ProductImage,Category,User
from rest_framework import viewsets
from .serializers import SellerSerializers,UserLocationSerializers,OrderItemsSerializers,OrderSerializers,ProductSerializers,ProductImageSerializers,CategorySerializers,UserSerializers
# Create your views here.
def home(requests):
    return HttpResponse('Hello world')
class SellerViewSet(viewsets.ModelViewSet):
    queryset=Seller.objects.all()
    serializer_class=SellerSerializers

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializers

class UserLocationViewSet(viewsets.ModelViewSet):
    queryset=UserLocation.objects.all()
    serializer_class=UserLocationSerializers

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializers

class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset=OrderItems.objects.all()
    serializer_class=OrderItemsSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset=ProductImage.objects.all()
    serializer_class=ProductImageSerializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializers
