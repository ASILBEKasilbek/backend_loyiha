from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register(r'Sellers',SellerViewSet),
router.register(r'Users',UserViewSet),
router.register(r'UserItemss',UserLocationViewSet),
router.register(r'Products',ProductViewSet),
router.register(r'ProductImages',ProductImageViewSet),
router.register(r'Orders',OrderViewSet),
router.register(r'OrderItemss',OrderItemsViewSet),
router.register(r'Categorys',CategoryViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('register/',RegisterView.as_view(), name='register'),
    path('send-verification-code/', SendVerificationCodeAPIView.as_view(), name='send-verification-code'),
    path('verify-code/', VerifyCodeAPIView.as_view(), name='verify-code'),
    path('stores/',StoreView.as_view(),name='store-list'),
    path('stores/<int:store_id>/books/',BookView.as_view(),name='book-list'),
    path('stores/<int:pk>/', StoreDetailView.as_view(), name='store-detail'),
]