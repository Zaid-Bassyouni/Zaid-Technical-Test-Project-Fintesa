
from django.shortcuts import render
from rest_framework.views import APIView 
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

User = get_user_model()

def get_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token)
    }



def homepage(request):
    
    return render(request, 'homepage.html')

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                UserSerializer(user).data, status=201
            )
        return Response(serializer.errors, status=400)


# -----------


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, requesr):
        serializer = LoginSerializer(data = requesr.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

        else:
            return Response(serializer.errors , status=400)
        user = User.objects.filter(email = email).first()
        if not user or not check_password(password,user.password):
            return Response( {"detail": "Inalid email or password"},status=401 )
        
        else:
            return Response(get_tokens(user) , status=200)
        
# -------------

class MeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,reqest):
        return Response(UserSerializer(reqest.user).data , status=200)
    
# -------------

class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user and user.is_authenticated and user.roles.filter(name="admin").exists())

class AdminView(APIView):
    permission_classes = [IsAdminRole]

    def get(self,request):
        return Response({"message" : f"Welcome admin {request.user.username}"} , status=200)
    
# -------------
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return Response(status=204)


# --------- Extra Functionalities to test --------

def register_form(request):
    return render(request, "register_form.html")

def login_form(request):
    return render(request, "login_form.html")