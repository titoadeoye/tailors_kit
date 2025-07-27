from rest_framework import serializers
from media_file.models import MediaFile


class MediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = ["id", "url", "uploaded_by", "file_type", "date_created"]
