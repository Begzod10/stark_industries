from rest_framework.routers import DefaultRouter

from accounting.payment.views import PaymentViewSet

router = DefaultRouter()
router.register(r'payment'
                , PaymentViewSet, basename='payment')

urlpatterns = router.urls
