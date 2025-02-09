from django.contrib import admin

from .models import AnalysisType, Packet, Container, Analysis


@admin.register(AnalysisType)
class AnalysisTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'branch')
    search_fields = ('name', 'branch__name')
    list_filter = ('branch',)


@admin.register(Packet)
class PacketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'branch')
    search_fields = ('name', 'branch__name')
    list_filter = ('branch',)


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'size', 'branch')
    search_fields = ('name', 'color', 'size', 'branch__name')
    list_filter = ('branch', 'color', 'size')


@admin.register(Analysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device', 'packet', 'price', 'type', 'container', 'code_name', 'branch')
    search_fields = ('name', 'code_name', 'device__name', 'packet__name', 'branch__name')
    list_filter = ('branch', 'type', 'device', 'packet')
