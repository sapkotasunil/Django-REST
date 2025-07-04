import django_filters
from .models import Employee


class EmplyeeFilter(django_filters.FilterSet):
    designaton=django_filters.CharFilter(field_name='designation',lookup_expr='iexact') #field_name='designation' tells Django which field in the model to filter. lookup_expr='iexact' means case-insensitive exact match (e.g., 'Manager' will match 'manager').
    emp_name=django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')   #lookup_expr='icontains' means it will do a case-insensitive partial match — like a search. Example: if you search sun, it will match 'Sunil', 'Sundar', 'sunita', etc.
    id=django_filters.RangeFilter(field_name='id')
    class Meta:
        model=Employee
        fields=['designation','emp_name','id']