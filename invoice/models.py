from django.db import models

from users.models import ExtendedUser


class Invoice(models.Model):
    number = models.CharField(
        'numer faktury',
        max_length=50
    )
    payment_date = models.DateField(
        'termin płatności'
    )
    supplier = models.CharField(
        'nazwa firmy',
        max_length=50,
        default=''
    )
    amount = models.DecimalField(
        'kwota',
        decimal_places=2,
        max_digits=8,
        default=''
    )
    is_paid = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.number

