from django.db import models
from django.conf import settings
from media_file.models import MediaFile


# Create your models here.
class Inventory(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="inventory"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    yards = models.FloatField()
    picture = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="inventory_photos",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
