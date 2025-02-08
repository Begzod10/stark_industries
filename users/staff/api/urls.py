from django.urls import path, include
from users.staff.api.crud.create import StaffRegisterView
from users.staff.api.crud.update import StaffUpdateView, StaffUpdatePasswordView
from users.staff.api.crud.destroy import StaffDestroyView
from users.staff.api.get.get import StaffListView, StaffDetailView, StaffListDeletedView

urlpatterns = [
    path('create/', StaffRegisterView.as_view(), name='staff_create'),
    path('update/<int:pk>', StaffUpdateView.as_view(), name='staff_update'),
    path('update_password/<int:pk>', StaffUpdatePasswordView.as_view(), name='staff_update'),
    path('delete/<int:pk>', StaffDestroyView.as_view(), name='staff_delete'),
    path('get_list/', StaffListView.as_view(), name='staff_list'),
    path('get_deleted_list/', StaffListDeletedView.as_view(), name='staff_deleted_list'),
    path('get_detail/<int:pk>', StaffDetailView.as_view(), name='staff_detail'),
]
