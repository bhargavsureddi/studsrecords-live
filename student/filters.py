import django_filters
from .models import Student
from django_filters import NumberFilter,CharFilter
class StudentFilter(django_filters.FilterSet):
    cgpa_gte_n=NumberFilter(field_name="cgpa",lookup_expr="gte")
    name=CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model=Student
        fields="__all__"
        exclude=["cgpa"]

