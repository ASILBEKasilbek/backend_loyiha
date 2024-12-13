from django.shortcuts import render,HttpResponse
from .models import *
from rest_framework import viewsets,status
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PhoneNumberSerializer, VerificationCodeSerializer
from .utils import generate_verification_code, send_sms

class SendVerificationCodeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = PhoneNumberSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            code = generate_verification_code()
            verification_entry, created = UserPhoneVerification.objects.get_or_create(phone_number=phone_number)
            verification_entry.verification_code = code
            verification_entry.save()
            send_sms(phone_number, code)
            return Response({'message': 'Verification code sent successfully!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyCodeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = VerificationCodeSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            verification_code = serializer.validated_data['verification_code']

            try:
                entry = UserPhoneVerification.objects.get(phone_number=phone_number)
                if entry.verification_code == verification_code:
                    entry.is_verified = True
                    entry.save()
                    return Response({'message': 'Phone number verified successfully!'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
            except UserPhoneVerification.DoesNotExist:
                return Response({'error': 'Phone number not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
