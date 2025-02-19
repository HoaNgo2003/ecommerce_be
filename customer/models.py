import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class Customer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone"]  # Fields required when creating a superuser

    def __str__(self):
        return self.email

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # UUID as primary key
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='job')
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.title} at {self.company}"
