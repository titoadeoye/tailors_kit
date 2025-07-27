from rest_framework import serializers
from users.models import User
from media_file.serializers import MediaFileSerializer

class UserSerializer(serializers.ModelSerializer):
    profile_picture = MediaFileSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'role',
            'date_created', 'date_updated',
            'profile_picture',
        ]
