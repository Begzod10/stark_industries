from django.urls import path, include

from users.users.api.crud.update import UsersUpdateView
from users.users.api.crud.delete import UserDestroyView

urlpatterns = [
    path('update/<int:pk>', UsersUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', UserDestroyView.as_view(), name='delete'),
]
