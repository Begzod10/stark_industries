from django.urls import path

from users.users.api.crud.update import UsersUpdateView
from users.users.api.crud.delete import UserDestroyView
from users.users.api.crud.create import UserRegisterView, UseraddRequest

urlpatterns = [
    path('create/', UserRegisterView.as_view(), name='create'),
    path('add_user_request/', UseraddRequest.as_view(), name='add_user_request'),
    path('update/<int:pk>', UsersUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', UserDestroyView.as_view(), name='delete'),
    path('delete_request/<int:pk>', UserDestroyView.as_view(), name='delete'),
]
