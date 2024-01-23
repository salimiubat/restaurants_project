from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'role', 'phone_number', 'address', 'is_verified', 'password')

        extra_kwargs = {
            "email": {"required": True, "unique": True},
            "password": {"write_only": True},
        }

    def validate_email(self, value):
        existing_users = User.objects.filter(email=value)
        if self.instance:
            existing_users = existing_users.exclude(pk=self.instance.pk)

        if existing_users.exists():
            raise serializers.ValidationError("This email address is already in use.")

        return value

    def create(self, validated_data):
        email = validated_data.get('email')
        if email.endswith('@example.com'):
            validated_data['role'] = User.UserTypes.Owner
            validated_data['is_staff'] = True
            validated_data['is_superuser'] = True
        else:
            validated_data['role'] = User.UserTypes.EMPLOYEE

        validated_data['password'] = make_password(validated_data['password'])

        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return data
