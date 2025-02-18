from drf_yasg.utils import swagger_auto_schema
from drf_spectacular.utils import extend_schema  # Alternative for Spectacular
from rest_framework import generics
from .models import Book, Phone, Clothes
from .serializers import BookSerializer, PhoneSerializer, ClothesSerializer

# 📚 Base Views for Products
class BaseProductListCreateView(generics.ListCreateAPIView):
    """Base view for listing and creating product instances."""
    def get_queryset(self):
        return self.model.objects.all()

class BaseProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Base view for retrieving, updating, and deleting product instances."""
    def get_queryset(self):
        return self.model.objects.all()

# 📚 Books API
@extend_schema(tags=["Books"])
class BookListCreateView(BaseProductListCreateView):
    model = Book
    serializer_class = BookSerializer  # Use BookSerializer

@extend_schema(tags=["Books"])
class BookDetailView(BaseProductDetailView):
    model = Book
    serializer_class = BookSerializer  # Use BookSerializer

# 📱 Phones API
@extend_schema(tags=["Phones"])
class PhoneListCreateView(BaseProductListCreateView):
    model = Phone
    serializer_class = PhoneSerializer  # Use PhoneSerializer

@extend_schema(tags=["Phones"])
class PhoneDetailView(BaseProductDetailView):
    model = Phone
    serializer_class = PhoneSerializer  # Use PhoneSerializer

# 👕 Clothes API
@extend_schema(tags=["Clothes"])
class ClothesListCreateView(BaseProductListCreateView):
    model = Clothes
    serializer_class = ClothesSerializer  # Use ClothesSerializer

@extend_schema(tags=["Clothes"])
class ClothesDetailView(BaseProductDetailView):
    model = Clothes
    serializer_class = ClothesSerializer  # Use ClothesSerializer
