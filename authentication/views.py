from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from users.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth import login as django_login

@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    VALID_ROLES = [choice[0] for choice in User.role_choices]

    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    password = request.data.get("password")
    email = request.data.get("email")
    role = request.data.get("role", "tailor")
    username = request.data.get("username")  # optional

    if not first_name or not password or not email:
        return Response(
            {"error": "First name, password and email are required."}, status=400
        )

    if role not in VALID_ROLES:
        return Response(
            {"error": f"Invalid role. Must be one of: {VALID_ROLES}"}, status=400
        )

    # if username not provided, generate one
    if not username:
        while True:
            username = get_random_string(10)
            if not User.objects.filter(username=username).exists():
                break

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        password=password,
        email=email,
        role=role,
    )
    token, created = Token.objects.get_or_create(user=user)
    return Response(
        {
            "token": token.key,
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "first_name": user.first_name,
                "last_name": user.last_name,
            },
        }
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=400)

    if user.check_password(password):
        # ✅ Create session
        django_login(request, user)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                },
            }
        )
    else:
        return Response({"error": "Invalid credentials"}, status=400)
