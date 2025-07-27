from rest_framework import serializers
from catalogue.models import CatalogueItem
from media_file.serializers import MediaFileSerializer


class CatalogueItemSerializer(serializers.ModelSerializer):
    picture = MediaFileSerializer(read_only=True)

    class Meta:
        model = CatalogueItem
        fields = "__all__"
