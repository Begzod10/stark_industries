from rest_framework.routers import DefaultRouter

from users.patients.api import PatientViewSet

router = DefaultRouter()
router.register(r'payment'
                , PatientViewSet, basename='payment')

urlpatterns = router.urls
