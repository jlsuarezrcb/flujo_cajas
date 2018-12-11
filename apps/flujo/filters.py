import django_filters
from django import forms

from apps.flujo import models


class ActivoFilter(django_filters.FilterSet):

    class Meta:
        model = models.Activo
        fields = {
            'nombre_activo': ['icontains'], #contain, exact, iexact, lte, gte, lt, gt
             #'valor_activo': ['lte','gte'],
            # 'close_time': ['lte','gte'],
}
