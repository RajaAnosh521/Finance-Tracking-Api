from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import authenticate

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),  
    }


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password) 
        if user is not None:
            tokens = get_tokens_for_user(user)
            return Response({"message": "User logged in successfully", "token": tokens}, status.HTTP_200_OK) 
        return Response({"message": "Invalid credentials"}, status.HTTP_401_UNAUTHORIZED)
    

class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # Blacklists the refresh token
            return Response({"message": "User logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token or token already blacklisted"}, status=status.HTTP_400_BAD_REQUEST)