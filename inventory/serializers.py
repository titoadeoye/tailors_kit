from rest_framework import serializers
from inventory.models import Inventory
from media_file.serializers import MediaFileSerializer


class InventorySerializer(serializers.ModelSerializer):
    picture = MediaFileSerializer(read_only=True)

    class Meta:
        model = Inventory
        fields = "__all__"
