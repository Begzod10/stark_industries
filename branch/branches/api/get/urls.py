from django.urls import path
from branch.branches.api.get.list import BranchListView

urlpatterns = [
    path('', BranchListView.as_view()),
]
