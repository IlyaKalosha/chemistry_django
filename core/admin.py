from django.contrib import admin
from django.contrib.auth.models import User

from .models import Pharmacy, Manager, Recipe, Pill, Seller, Order, Basket, Storage


@admin.register(Pharmacy)
class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['city', 'address', 'zip', 'phone']
    search_fields = ['city', 'address', 'zip', 'phone']


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'pharmacy_id']
    search_fields = ['__str__', 'phone', 'pharmacy_id']


@admin.register(Pill)
class PillAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'category', 'country', 'barcode', 'info']
    search_fields = ['name', 'cost', 'category', 'country', 'barcode', 'info']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'manager_id']
    search_fields = ['__str__', 'phone', 'manager_id']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(is_staff=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'seller_id', 'manager_id', 'pharmacy_id', 'is_agreed', 'date']
    search_fields = ['id', 'seller_id', 'manager_id', 'pharmacy_id', 'is_agreed', 'date']

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pharmacy_id=request.user.manager.pharmacy_id)


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):

    list_display = ['pill_id', 'order_id', 'count']
    search_fields = ['pill_id', 'order_id', 'count']

    def get_queryset(self, request):
        qs = super(BasketAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(order_id__pharmacy_id=request.user.manager.pharmacy_id, order_id__is_agreed=False)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'pill_name', 'signature', 'expire_date']
    search_fields = ['doctor', 'pill_name', 'signature', 'expire_date']


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['pill_id', 'count', 'pharmacy_id']
    search_fields = ['pill_id', 'count', 'pharmacy_id']

    def get_queryset(self, request):
        qs = super(StorageAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pharmacy_id=request.user.manager.pharmacy_id)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "pharmacy_id":
            kwargs["queryset"] = Pharmacy.objects.filter(id=request.user.manager.pharmacy_id.id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


