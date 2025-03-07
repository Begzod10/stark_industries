from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import UserJobs, UserAnalysis, User, UserRequest


@admin.register(UserJobs)
class UserJobsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserJobs._meta.fields]
    list_filter = [field.name for field in UserJobs._meta.fields if field.get_internal_type() != "TextField"]
    search_fields = ('user__name', 'job__title')


@admin.register(UserAnalysis)
class UserAnalysisAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserAnalysis._meta.fields]
    list_filter = [field.name for field in UserAnalysis._meta.fields if field.get_internal_type() != "TextField"]
    search_fields = ('user__name', 'analysis__name')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]
    list_filter = [field.name for field in User._meta.fields if field.get_internal_type() != "TextField"]
    search_fields = ('username', 'name', 'surname', 'phone_number')
    ordering = ('id',)


@admin.register(UserRequest)
class UserRequestAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserRequest._meta.fields]
    list_filter = [field.name for field in UserRequest._meta.fields if field.get_internal_type() != "TextField"]
    search_fields = ('doctor__name', 'patient__name')
