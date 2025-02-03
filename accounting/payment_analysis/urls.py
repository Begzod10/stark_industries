from rest_framework.routers import DefaultRouter

from accounting.payment_analysis.views import PaymentAnalysisViewSet

router = DefaultRouter()
router.register(r'payment_analysis'
                , PaymentAnalysisViewSet, basename='payment_analysis')

urlpatterns = router.urls