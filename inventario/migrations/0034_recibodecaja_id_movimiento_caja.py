# Generated by Django 3.2.9 on 2022-10-26 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0033_remove_recibodecaja_id_movimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='recibodecaja',
            name='id_movimiento_caja',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inventario.caja'),
        ),
    ]
