# Generated by Django 4.2.1 on 2023-10-20 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=200)),
                ('equipo', models.CharField(max_length=200)),
                ('ubicacion', models.CharField(max_length=200)),
                ('sede', models.CharField(max_length=200)),
                ('etiqueta_caja', models.CharField(max_length=200)),
                ('factura_contrato', models.CharField(max_length=200)),
                ('resolucion_invima', models.CharField(max_length=200)),
                ('carta_garantia', models.CharField(max_length=200)),
                ('acta_entrega', models.CharField(max_length=200)),
                ('declaracion_importacion', models.CharField(max_length=200)),
                ('cronograma_mantenimiento', models.CharField(max_length=200)),
                ('cronograma_calibracion', models.CharField(max_length=200)),
                ('reportes_mantenimiento', models.CharField(max_length=200)),
                ('reportes_calibracion', models.CharField(max_length=200)),
                ('guia_rapida', models.CharField(max_length=200)),
                ('manual_usuario_espanol', models.CharField(max_length=200)),
                ('manual_servicio_espanol', models.CharField(max_length=200)),
                ('hoja_vida_calibracion', models.CharField(max_length=200)),
                ('hoja_vida_mantenimiento', models.CharField(max_length=200)),
                ('contrato_mantenimiento', models.CharField(max_length=200)),
                ('contrato_calibracion', models.CharField(max_length=200)),
            ],
        ),
    ]
