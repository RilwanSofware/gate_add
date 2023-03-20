from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Wallet(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    currency = models.CharField(max_length=50, default='NGN')
    created_at = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.user.__str__()
    
class Transaction(models.Model):

    TRANSACTION_TYPES = (
        ('deposit', 'deposit'),
        ("transfer","transfer"),
        ("withdraw", "withdraw"),
    )

    wallet = models.ForeignKey(Wallet, null=True, on_delete=models.CASCADE)
    trans_type = models.CharField(max_length=200, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=100, null=True, decimal_places=2)
    timestamp = models.DateField(default=timezone.now, null=True)
    status = models.CharField(default='pending', max_length=100)
    payment_ref = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.wallet.user.__str__()