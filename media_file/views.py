from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from media_file.models import MediaFile
from media_file.serializers import MediaFileSerializer

class MediaFileViewSet(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
