from django.db import models
from django.conf import settings
from customers.models import Customer


# Create your models here.
class Order(models.Model):
    currency_choices = (("NGN", "NGN"), ("USD", "USD"))
    status = (
        ("in_progress", "In progress"),
        ("completed", "Completed"),
        ("not_started", "Not started"),
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="orders"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    downpayment = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text="Amount paid as downpayment",
    )
    currency = models.CharField(max_length=10, default="NGN")
    due_date = models.DateField(help_text="When the order is meant to be delivered")
    notes = models.TextField(blank=True)
    is_fully_paid = models.BooleanField(
        default=False, help_text="Has the full payment been completed?"
    )

    date_downpayment_paid = models.DateField(
        null=True, blank=True, help_text="Date the downpayment was actually paid"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order for  {self.customer.name} on {self.date_created}"
