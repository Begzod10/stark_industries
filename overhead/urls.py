from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import OverheadViewSet, OverheadTypeViewSet

router = DefaultRouter()
router.register(r'overheads', OverheadViewSet, basename='overhead')
router.register(r'overhead-types', OverheadTypeViewSet, basename='overhead-type')

urlpatterns = [
    path('', include(router.urls)),
]
