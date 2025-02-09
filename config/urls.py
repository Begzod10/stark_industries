from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (

    TokenVerifyView, TokenRefreshView, TokenObtainPairView
)
from users.login.api.views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,

)

# from users.login.api.read import CustomTokenRefreshView
# from users.login.api.write import CustomTokenObtainPairView

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('config.utilis.swagger')),
    path('api/device/', include('device.device.api.urls')),
    path('api/user_job/', include('users.user_job.api.urls')),
    path('api/user_request/', include('users.user_request.api.urls')),
    path('api/branch_info/', include('branch.urls')),
    path('api/job_info/', include('job.urls')),
    path('api/user/', include('users.urls')),
    path('api/packet/', include('analysis.packet.api.urls')),
    path('api/container/', include('analysis.container.api.urls')),
    path('api/analysis/', include('analysis.urls')),
    path('api/account/', include('accounting.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
