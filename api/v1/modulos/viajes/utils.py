import django_filters
from .models import Viaje
from api.v1.modulos.omnibus.models import Omnibus

class ProductFilter(django_filters.FilterSet):
      class Meta:
        model = Viaje
        fields = ('hora','omnibus','chofer1','chofer2','origen','destino')