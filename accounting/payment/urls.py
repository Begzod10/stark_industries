from django.urls import path
from rest_framework.routers import DefaultRouter

from accounting.payment.views import PaymentViewSet, PaymentList,PaymentListUser

router = DefaultRouter()
router.register(r'payment'
                , PaymentViewSet, basename='payment')
urlpatterns = [
    path('payment_list/', PaymentList.as_view(), name='payment_list'),
    path('payment_list/<int:pk>/', PaymentListUser.as_view(), name='payment_list'),
]
urlpatterns += router.urls
