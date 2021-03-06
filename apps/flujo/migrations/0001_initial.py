# Generated by Django 2.0.7 on 2018-11-26 22:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acredor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Activo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_activo', models.CharField(max_length=255)),
                ('valor_activo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tiempo', models.CharField(choices=[('HORA', 'Hora'), ('DIA', 'Dia'), ('MES', 'Mes')], max_length=30)),
                ('valor_tiempo', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('SUMA', 'Suma'), ('RESTA', 'Resta')], max_length=30)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('nombre_dia', models.CharField(choices=[('LUNES', 'Lunes'), ('MARTES', 'Martes'), ('MIERCOLES', 'Miercoles'), ('JUEVES', 'Jueves'), ('VIERNES', 'Viernes'), ('SABADO', 'Sabado'), ('DOMINGO', 'Domingo')], max_length=30)),
                ('nombre', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Obligaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo_obligacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cuota_obligacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tiempo', models.CharField(choices=[('HORA', 'Hora'), ('DIA', 'Dia'), ('MES', 'Mes')], max_length=30)),
                ('valor_tiempo', models.PositiveIntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('tasa_obligacion', models.DecimalField(decimal_places=2, max_digits=10)),
                ('acredor_obligacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flujo.Acredor')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flujo.Categoria')),
            ],
        ),
        migrations.AddField(
            model_name='movimiento',
            name='subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flujo.SubCategoria'),
        ),
        migrations.AddField(
            model_name='activo',
            name='moneda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flujo.Moneda'),
        ),
    ]
