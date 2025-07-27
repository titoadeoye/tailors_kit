from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from users.models import User


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    password = request.data.get("password")
    email = request.data.get("email")
    role = request.data.get("role", "tailor")

    if not first_name or not password or not email:
        return Response(
            {"error": "First name, password and email are required."}, status=400
        )

    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        password=password,
        email=email,
        role=role,
    )
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, user: user})


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("meail")
    password = request.data.get("password")

    user = authenticate(email=email, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key, user: user})
    else:
        return Response({"error": "Invalid credentials"}, status=400)
