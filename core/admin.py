from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Pharmacy, Manager, Recipe, Pill, Seller, Order, Basket, Storage
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'zip', 'phone']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'pharmacy_id']


@admin.register(Pill)
class PillAdmin(admin.ModelAdmin):
    search_fields = ['name', 'category']


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
    list_display = ['doctor', 'pill_name', 'signature', 'expire_date']


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['pill_id', 'count', 'pharmacy_id']

    def get_queryset(self, request):
        qs = super(StorageAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pharmacy_id=request.user.manager.pharmacy_id)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "pharmacy_id":
            kwargs["queryset"] = Pharmacy.objects.filter(id=request.user.manager.pharmacy_id.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


