from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField() 
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': True,},
            'email': {'required': True, 'write_only': True} 
        } 

    def validate(self, data):
        if 'email' in data and User.objects.filter(email=data['email']).exists():
            raise ValidationError('email already exists')
        if 'password' in data and len(data['password']) < 8:
            raise ValidationError('Password must be at least 8 characters') 
        return data

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField() 

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'required': True}
        }

    def validate(self, data):
        if 'username' not in data and User.objects.filter(username=data['username']).exists():
            raise ValidationError('username does not exists!')
        if 'password' in data != User.objects.filter(password=data['password']): 
            raise ValidationError("password doesn't match!")  
        return data 