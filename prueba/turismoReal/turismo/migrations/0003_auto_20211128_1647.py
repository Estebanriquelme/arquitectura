# Generated by Django 3.2.9 on 2021-11-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0002_auto_20211128_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='precio_depto',
            field=models.IntegerField(default=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicioextra',
            name='precio_depto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transporte',
            name='precio_depto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]