from django.contrib import admin

from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'branch', 'ip_address', 'deleted')
    search_fields = ('name', 'ip_address', 'branch__name')
    list_filter = ('branch', 'deleted')
    list_editable = ('deleted',)
