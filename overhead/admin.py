from django.contrib import admin
from .models import Overhead, OverheadType


@admin.register(OverheadType)
class OverheadTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'id')
    list_editable = ('order',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('order', 'name')

    fieldsets = (
        (None, {
            'fields': ('name', 'order')
        }),
    )


@admin.register(Overhead)
class OverheadAdmin(admin.ModelAdmin):
    list_display = ('name', 'payment', 'created', 'price', 'price_formatted', 'branch', 'type', 'deleted')
    list_filter = ('deleted', 'branch', 'type', 'payment', 'created')
    search_fields = ('name',)
    list_editable = ('price',)  # Now matches with price in list_display
    date_hierarchy = 'created'
    ordering = ('-created',)
    autocomplete_fields = ('payment', 'branch', 'type')

    # Removed 'fields' and kept only 'fieldsets'
    fieldsets = (
        (None, {
            'fields': ('name', 'price', 'created')
        }),
        ('Relationships', {
            'fields': ('payment', 'branch', 'type')
        }),
        ('Status', {
            'fields': ('deleted',)
        }),
    )

    def price_formatted(self, obj):
        return f"{obj.price:,}" if obj.price is not None else "-"

    price_formatted.short_description = "Price"
    price_formatted.admin_order_field = 'price'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('payment', 'branch', 'type')