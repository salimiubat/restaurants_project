# views.py
from rest_framework import viewsets,status
from .models import Restaurant, Menu, MenuItem, Order, OrderItem, Payment
from rest_framework.permissions import IsAuthenticated

from .serializer import (
    RestaurantSerializer,
    MenuSerializer,
    MenuItemSerializer,
    OrderSerializer,
    PaymentSerializer
)
from rest_framework.response import Response

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        user = request.user

        if user.role == "OWNER":
            request.data['owner'] = user.id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("You are not allowed", status=status.HTTP_403_FORBIDDEN)


    def update(self, request, *args, **kwargs):
        user = request.user
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        # Check if the authenticated user is the owner and has the "OWNER" role
        if instance.owner == user and user.role == "OWNER":
            request.data['owner'] = user.id

            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("You are not allowed to update this restaurant.", status=status.HTTP_403_FORBIDDEN)
        
    def get_queryset(self):
        user = self.request.user
        return Restaurant.objects.filter(owner=user)

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Menu.objects.filter(restaurant__owner=user)

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return MenuItem.objects.filter(menu__restaurant__owner=user)
    


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
