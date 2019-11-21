import django_filters
from django_filters import rest_framework as filters
from .models import Goods


class GoodsFilter(filters.FilterSet):
    price_min = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')

    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
