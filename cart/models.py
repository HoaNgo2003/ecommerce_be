from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from customer.models import Customer  # Assuming you have a Customer model

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Add total price field

    def update_total_price(self):
        """Recalculate total price based on cart items."""
        self.total_price = sum(item.price_item for item in self.items.all())
        self.save()

    

class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, related_name="items")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    product = GenericForeignKey("content_type", "object_id")
    quantity = models.PositiveIntegerField(default=1)
    price_item = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        """Recalculate price_item before saving"""
        if self.product:
            self.price_item = self.quantity * self.product.price
        super().save(*args, **kwargs)
        self.cart.update_total_price()

    def delete(self, *args, **kwargs):
        """Update total price when item is deleted"""
        super().delete(*args, **kwargs)
        self.cart.update_total_price()