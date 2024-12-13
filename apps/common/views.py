from django.shortcuts import render,HttpResponse
from .models import *
from rest_framework import viewsets,status
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


class RegisterView(APIView):
    queryset=CustomUser.objects.all()
    serializer_class=CustomUserSerializer
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'message': 'Foydalanuvchi muvaffaqiyatli ro\'yxatdan o\'tdi',
                'user': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
