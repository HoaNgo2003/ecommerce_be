from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType
from .models import Cart, CartItem
from products.models import Book
from products.models import Phone
from products.models import Clothes

class CartItemSerializer(serializers.ModelSerializer):
    product_type = serializers.CharField(source="content_type.model", read_only=True)
    product_id = serializers.IntegerField(source="object_id")

    class Meta:
        model = CartItem
        fields = ["id", "product_type", "product_id", "quantity"]

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "customer", "items", "created_at"]
