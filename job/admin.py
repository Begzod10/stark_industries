from django.contrib import admin

from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'has_client')
    search_fields = ('name',)
    list_filter = ('has_client',)
    list_editable = ('has_client',)
