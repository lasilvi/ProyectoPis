# Generated by Django 4.2.6 on 2023-11-03 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppSeguimiento', '0003_remove_equipos_equipo_equipos_bio_equipos_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='porcentajedecumplimiento',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
