from django.db import models
from django.contrib.auth.models import AbstractUser
from media_file.models import MediaFile


# Create your models here.
class User(AbstractUser):
    role_choices = (
        (
            "tailor",
            "Tailor",
        ),  # the tailor / service worker who owns catalogue, customers, etc.
        (
            "viewer",
            "viewer",
        ),  # regular public user who can sign up to browse catalogues or posts
        ("admin", "Admin"),  # platform admin with full power
        ("Support", "support"),  # can moderate flagged posts, etc.
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        null=True,     # <- allow null in DB
        blank=True     # <- allow empty in forms
    )
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True)
    role = models.CharField(
        max_length=20,
        choices=role_choices,
        default="tailor",
        help_text="Role of the user in the system",
    )
    profile_picture = models.ForeignKey(
        MediaFile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="profile_users",
    )  # for AWS S3 link
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"
