import django_filters


from users.models.user import User


class UserFilter(django_filters.FilterSet):
    job_id = django_filters.NumberFilter(method='filter_by_job')

    class Meta:
        model = User
        fields = []

    def filter_by_job(self, queryset, name, value):
        return queryset.filter(userjobs__job_id=value)
