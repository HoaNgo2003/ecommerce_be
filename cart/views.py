from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from customer.models import Customer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        customer_id = request.data.get("customer_id")
        if not customer_id:
            return Response({"error": "Customer ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        customer = Customer.objects.filter(id=customer_id).first()
        if not customer:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(customer=customer)
        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        cart_id = request.data.get("cart_id")
        product_type = request.data.get("product_type")
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)

        cart = Cart.objects.filter(id=cart_id).first()
        if not cart:
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            content_type = ContentType.objects.get(model=product_type)
        except ContentType.DoesNotExist:
            return Response({"error": "Invalid product type"}, status=status.HTTP_400_BAD_REQUEST)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, content_type=content_type, object_id=product_id,
            defaults={"quantity": quantity}
        )

        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)
