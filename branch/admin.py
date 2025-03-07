from django.contrib import admin

from .models import Location, Branch


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'starts', 'ends', 'phone_number', 'ip_address', 'main')
    search_fields = ('name', 'phone_number', 'ip_address', 'location__name')
    list_filter = ('main', 'location',)
