from django_filters import rest_framework as filters, DateFromToRangeFilter, RangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # created_at_after = filters.DateFromToRangeFilter(field_name='created_at_after', lookup_expr='gte')
    # created_at_before = filters.DateFromToRangeFilter(field_name='created_at_before', lookup_expr='lte')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']

