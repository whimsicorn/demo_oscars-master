import django_tables2 as tables
from app_oscars.models import Review
import django_filters

class ReviewTable(tables.Table):
    class Meta:
        model = Review
        template_name = "django_tables2/bootstrap.html"
        fields = ('films', 'user', 'points')

class ReviewFilter(django_filters.FilterSet):
    class Meta:
        model = Review
        fields = ('films', 'user', 'points')

