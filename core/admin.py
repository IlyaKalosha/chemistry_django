from django.contrib import admin
from .models import Pharmacy, Manager, Recipe, Pill, Seller, Order, Basket, Storage
from django.contrib.auth.models import Group, User


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    pass


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    pass


@admin.register(Pill)
class PillAdmin(admin.ModelAdmin):
    search_fields = ['end_date']
    fields = []


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_staff=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    pass


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    pass

