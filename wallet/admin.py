from django.contrib import admin

from .models import Transaction, Wallet

# Register your models here.

admin.site.register(Wallet)
admin.site.register(Transaction)