from django.db import models
from django.conf import settings
from media_file.models import MediaFile


# Create your models here.
class CatalogueItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="catalogue_items",
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    picture = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="catalogue_photos",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
