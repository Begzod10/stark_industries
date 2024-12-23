from django.urls import path

from users.users.api.crud.update import UsersUpdateView
from users.users.api.crud.delete import UserDestroyView
from users.users.api.crud.create import UserRegisterView


urlpatterns = [
    path('create/', UserRegisterView.as_view(), name='create'),
    path('update/<int:pk>', UsersUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', UserDestroyView.as_view(), name='delete'),
]
