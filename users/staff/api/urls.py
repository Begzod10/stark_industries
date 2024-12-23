from django.urls import path, include
from users.staff.api.crud.create import StaffRegisterView
from users.staff.api.crud.update import StaffUpdateView
from users.staff.api.crud.destroy import StaffDestroyView
from users.staff.api.get.get import StaffListView, StaffDetailView

urlpatterns = [
    path('create/', StaffRegisterView.as_view(), name='staff_create'),
    path('update/<int:id>', StaffUpdateView.as_view(), name='staff_update'),
    path('delete/<int:id>', StaffDestroyView.as_view(), name='staff_delete'),
    path('get_list/', StaffListView.as_view(), name='staff_list'),
    path('get_detail/<int:id>', StaffDetailView.as_view(), name='staff_detail'),
]
