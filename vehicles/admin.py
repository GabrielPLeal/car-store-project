from django.contrib import admin
from .models import Vehicle, Customer


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    ...


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    ...
