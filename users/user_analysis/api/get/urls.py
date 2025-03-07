from django.urls import path
from users.user_analysis.api.get.list import UsersAnalysisList

urlpatterns = [
    path('', UsersAnalysisList.as_view()),
]
