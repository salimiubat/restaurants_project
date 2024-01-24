# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RestaurantViewSet,
    MenuViewSet,
    MenuItemViewSet,
    OrderViewSet,
    PaymentViewSet,
    # OrderItemViewSet
)

router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet, basename='restaurant')
router.register(r'menus', MenuViewSet, basename='menu')
router.register(r'items', MenuItemViewSet, basename='item')
router.register(r'orders', OrderViewSet,basename="orders")
# router.register(r'orders_item', OrderItemViewSet,basename="orders_item")

router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
