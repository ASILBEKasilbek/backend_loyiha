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
]