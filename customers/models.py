from django.db import models
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    MEASUREMENT_UNIT_CHOICES = [
        ("metric", "Metric (cm)"),
        ("imperial", "Imperial (inches)"),
    ]

    GENDER_CHOICES = [("male", "Male"), ("female", "Female")]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customers"
    )
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    note = models.TextField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    measurements = models.JSONField(default=dict, blank=True)
    measurement_unit = models.CharField(
        max_length=10, choices=MEASUREMENT_UNIT_CHOICES, default="metric"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
