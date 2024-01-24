# serializers.py
from rest_framework import serializers
from .models import *

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
       


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'

# class OrderItemSerializer(serializers.ModelSerializer):
#     total_amount = serializers.SerializerMethodField()

#     class Meta:
#         model = OrderItem
#         fields = '__all__'
#     def get_total_amount(self, obj):
#         total_amount = obj.menu_item.price * obj.quantity
#         return total_amount

class OrderSerializer(serializers.ModelSerializer):
    # order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
