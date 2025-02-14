from django.urls import path
from .views import (
    BookListCreateView, BookDetailView,
    PhoneListCreateView, PhoneDetailView,
    ClothesListCreateView, ClothesDetailView,
    ProductImageCreateView,
)

urlpatterns = [
    # Books
    path("books/", BookListCreateView.as_view(), name="book-list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # Phones
    path("phones/", PhoneListCreateView.as_view(), name="phone-list"),
    path("phones/<int:pk>/", PhoneDetailView.as_view(), name="phone-detail"),

    # Clothes
    path("clothes/", ClothesListCreateView.as_view(), name="clothes-list"),
    path("clothes/<int:pk>/", ClothesDetailView.as_view(), name="clothes-detail"),

    # Product Images
    path("images/upload/", ProductImageCreateView.as_view(), name="upload-image"),
]
