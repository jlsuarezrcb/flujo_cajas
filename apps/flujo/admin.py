from django.contrib import admin

# Register your models here.

from apps.flujo import models


class MonedaAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais')
    list_filter = ('nombre', 'pais')
    search_fields = ('nombre',)
    ordering = ('pais',)

class ObligacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion','acredor_obligacion',)


admin.site.register(models.Moneda,MonedaAdmin)
admin.site.register(models.Activo)
admin.site.register(models.Categoria)
admin.site.register(models.SubCategoria)
admin.site.register(models.Acredor)
admin.site.register(models.Movimiento)
admin.site.register(models.Obligaciones,ObligacionesAdmin)

