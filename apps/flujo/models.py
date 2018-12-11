
from django.db import models
from apps.flujo import properties



# Create your models here.
class Moneda(models.Model):
    pais = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Activo(models.Model):
    nombre_activo = models.CharField(max_length=255)
    valor_activo = models.DecimalField(decimal_places=2,max_digits=10)
    moneda = models.ForeignKey(Moneda,on_delete=models.CASCADE)
    tiempo = models.CharField(max_length=30,choices=properties.TIPO_TIEMPO)
    valor_tiempo =  models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_activo


class Acredor(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return self.nombre + " cedula:"+ self.cedula
    

class Obligaciones(models.Model):
    acredor_obligacion = models.ForeignKey(Acredor, on_delete=models.CASCADE)
    saldo_obligacion =models.DecimalField(decimal_places=2,max_digits=10)
    cuota_obligacion = models.DecimalField(decimal_places=2,max_digits=10)
    tiempo = models.CharField(max_length=30, choices=properties.TIPO_TIEMPO)
    valor_tiempo = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=500)
    tasa_obligacion = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)





class Categoria(models.Model):
    tipo = models.CharField(max_length=30, choices=properties.TIPO_MOVIMIENTO)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Movimiento(models.Model):
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    fecha = models.DateField()
    nombre_dia = models.CharField(max_length=30, choices=properties.TIPO_DIA_SEMANA)
    nombre = models.CharField(max_length=200)
    valor = models.DecimalField(decimal_places=2,max_digits=10)



