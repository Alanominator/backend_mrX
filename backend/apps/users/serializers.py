from django.contrib.auth.models import User
from rest_framework import serializers
from .models import CUser
from django.contrib.auth import authenticate
from django.conf import settings

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CUser
        fields = ('id', 'email', 'password')

# register user serializer
class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CUser
        fields = ('email', 'first_name', 'user_name', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        user = CUser.objects.create_user(
            validated_data['email'],
            validated_data['first_name'],
            validated_data['user_name'],
            validated_data['password'],
            )
        
        return user

class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")