# Generated by Django 3.2.9 on 2022-09-26 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0020_ventas_nombre_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas',
            name='nombre_vendedor',
            field=models.CharField(default=None, max_length=250, verbose_name='nombre_vendedor'),
        ),
    ]
