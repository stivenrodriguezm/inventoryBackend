# Generated by Django 3.2.9 on 2022-10-26 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0036_comprobantesdeegreso'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobantesdeegreso',
            name='id_movimiento_caja',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.caja'),
        ),
    ]