from rest_framework.routers import DefaultRouter

from accounting.payment_types.api.retrieve import PaymentTypeRetrieveViewSet

router = DefaultRouter()
router.register(r'payment_type'
                , PaymentTypeRetrieveViewSet, basename='payment_type')

urlpatterns = router.urls
