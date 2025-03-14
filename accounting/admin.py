from django.contrib import admin

from .models import PaymentType, Payment, PaymentAnalysis


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_type')
    search_fields = ('payment_type',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_type', 'amount', 'date', 'user', 'branch', 'deleted')
    list_filter = ('payment_type', 'date', 'branch', 'deleted')
    search_fields = ('user__username', 'branch__name')


@admin.register(PaymentAnalysis)
class PaymentAnalysisAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment', 'analysis', 'payment_type', 'amount', 'date', 'user_id', 'price')
    list_filter = ('payment_type', 'date')
    search_fields = ('user_id__username', 'payment__id')
