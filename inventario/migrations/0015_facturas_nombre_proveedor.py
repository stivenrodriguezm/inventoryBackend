# Generated by Django 3.2.9 on 2022-07-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0014_auto_20220709_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturas',
            name='nombre_proveedor',
            field=models.CharField(max_length=50, null=True),
        ),
    ]