from django.urls import path, include

urlpatterns = [
    path('payment/', include('accounting.payment.urls')),
    path('payment_analysis/', include('accounting.payment_analysis.urls')),
    path('payment_types/', include('accounting.payment_types.api.urls')),
    path('storage/', include('accounting.storage.urls')),
]
