from django.contrib import admin

from .models import TimeTable


@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
