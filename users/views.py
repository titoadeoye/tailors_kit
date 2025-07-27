from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from django.db import models
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from orders.models import Order
from inventory.models import Inventory
from catalogue.models import CatalogueItem
from customers.models import Customer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def user_metrics(request):
    user = request.user

    total_orders = Order.objects.filter(user=user).count()
    total_revenue = (
        Order.objects.filter(user=user, is_fully_paid=True).aggregate(
            total=models.Sum("amount")
        )["total"]
        or 0
    )
    total_inventory_yards = (
        Inventory.objects.filter(user=user).aggregate(total=models.Sum("yards"))[
            "total"
        ]
        or 0
    )
    catalogue_items = CatalogueItem.objects.filter(user=user).count()
    total_customers = Customer.objects.filter(user=user).count()

    return Response(
        {
            "total_orders": total_orders,
            "total_revenue": total_revenue,
            "total_inventory_yards": total_inventory_yards,
            "catalogue_items": catalogue_items,
            "total_customers": total_customers,
        }
    )
