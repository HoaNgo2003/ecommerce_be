from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from products.models import Product, Book, Phone, Clothes
from .serializers import CartSerializer, CartItemSerializer
from customer.models import Customer
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):
        customer_id = request.data.get("customer")
        if not customer_id:
            return Response({"error": "Customer ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        customer = get_object_or_404(Customer, id=customer_id)
        cart, created = Cart.objects.get_or_create(customer=customer)

        # Update the total price after creating the cart
        cart.update_total_price()

        return Response(CartSerializer(cart).data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        # Make sure total_price is not included in the request data
        request.data.pop('total_price', None)  # Remove total_price from the data if it exists
        return super().update(request, *args, **kwargs)



class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def create(self, request, *args, **kwargs):
        cart_id = request.data.get("cart_id")
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        cart = Cart.objects.filter(id=cart_id).first()
        if not cart:
            return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

        # Lấy đúng subclass của Product
        product = None
        for model in [Book, Phone, Clothes]:  # Thêm các model khác nếu có
            product = model.objects.filter(id=product_id).first()
            if product:
                break

        if not product:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        # Kiểm tra hàng tồn kho
        if quantity > product.stock:
            return Response({"error": f"Only {product.stock} items left in stock"}, status=status.HTTP_400_BAD_REQUEST)

        # Lấy ContentType cho sản phẩm
        content_type = ContentType.objects.get_for_model(product)

        # Kiểm tra nếu sản phẩm đã có trong giỏ hàng
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart, content_type=content_type, object_id=product.id,
            defaults={"quantity": quantity}
        )

        if not created:
            if  quantity > product.stock:
                return Response({"error": f"Cannot add {quantity} items. Only {product.stock - cart_item.quantity} left in stock."},
                                status=status.HTTP_400_BAD_REQUEST)

            cart_item.quantity += quantity
            cart_item.price_item = cart_item.quantity * product.price
            cart_item.save()

        # 🟢 Cập nhật stock của sản phẩm
        product.stock -= quantity
        product.save()
        return Response(CartItemSerializer(cart_item).data, status=status.HTTP_201_CREATED)