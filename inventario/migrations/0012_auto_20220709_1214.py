# Generated by Django 3.2.9 on 2022-07-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_auto_20220319_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='tablado',
        ),
        migrations.AddField(
            model_name='productos',
            name='medidas',
            field=models.CharField(default=None, max_length=255, verbose_name='medidas'),
        ),
    ]