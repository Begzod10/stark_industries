from django.urls import path, include
from users import views

urlpatterns = [
    path('users/crud/', include('users.users.api.crud.urls')),
    path('staff/crud/', include('users.staff.api.urls')),
    path('username-check/', views.UsernameCheck.as_view(), name='username_check'),
    path('username-check-authorized/', views.UsernameCheckAuthorized.as_view(), name='username_check_authorized'),
]
