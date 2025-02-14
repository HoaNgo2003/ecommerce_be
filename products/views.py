from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema  # Alternative for Spectacular
from rest_framework import generics
from .models import Book, Phone, Clothes, ProductImage
from .serializers import BookSerializer, PhoneSerializer, ClothesSerializer, ProductImageSerializer

# 📚 Books API
@extend_schema(tags=["Books"])
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@extend_schema(tags=["Books"])
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# 📱 Phones API
@extend_schema(tags=["Phones"])
class PhoneListCreateView(generics.ListCreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

@extend_schema(tags=["Phones"])
class PhoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

# 👕 Clothes API
@extend_schema(tags=["Clothes"])
class ClothesListCreateView(generics.ListCreateAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

@extend_schema(tags=["Clothes"])
class ClothesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer

# 🖼️ Product Image Upload API
@extend_schema(tags=["Product Images"])
class ProductImageCreateView(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
