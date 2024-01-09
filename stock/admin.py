from django.contrib import admin

# Register your models here.
from django.contrib import admin

from stock.models import Stock
from stock.models import Currency
from stock.models import (Account, AccountCurrency, AccountStock)



@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
     list_display = ("ticker", "name", "description")
     pass

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountCurrency)
class AccountCurrencyAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountStock)
class AccountStockAdmin(admin.ModelAdmin):
    pass


class AccountCurrencyInline(admin.TabularInline):
    model = AccountCurrency


class AccountStockInline(admin.TabularInline):
    model = AccountStock


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    inlines = [AccountCurrencyInline, AccountStockInline]
