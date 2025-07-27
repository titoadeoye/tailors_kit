from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from inventory.models import Inventory
from inventory.serializers import InventorySerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
