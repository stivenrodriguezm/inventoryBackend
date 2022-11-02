# Generated by Django 3.2.9 on 2022-10-25 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0028_recibodecaja'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recibodecaja',
            name='saldo_cancelacion',
        ),
        migrations.AddField(
            model_name='recibodecaja',
            name='abono_cancelacion',
            field=models.CharField(max_length=50, null=True, verbose_name='abono_cancelacion'),
        ),
    ]