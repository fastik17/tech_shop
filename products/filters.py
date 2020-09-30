from django_filters import rest_framework as filters

from products.models import Product


class DateProductFilter(filters.FilterSet):
    date = filters.DateFromToRangeFilter()

    class Meta:
        model = Product
        fields = ['created_at']
