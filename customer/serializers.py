from rest_framework import serializers
from .models import Customer
from .models import Customer, Address, Job

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = ['email', 'username', 'password']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class CustomerSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Customer
        exclude = ['password']  
