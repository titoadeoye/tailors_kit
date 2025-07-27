from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from catalogue.models import CatalogueItem
from catalogue.serializers import CatalogueItemSerializer

class CatalogueItemViewSet(viewsets.ModelViewSet):
    queryset = CatalogueItem.objects.all()
    serializer_class = CatalogueItemSerializer
