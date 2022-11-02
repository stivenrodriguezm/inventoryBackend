# Generated by Django 3.2.9 on 2022-07-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0017_facturas_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transportadores',
            name='telefono_tranportador',
        ),
        migrations.AddField(
            model_name='transportadores',
            name='telefono_transportador',
            field=models.CharField(max_length=250, null=True, verbose_name='telefono_transportador'),
        ),
    ]
