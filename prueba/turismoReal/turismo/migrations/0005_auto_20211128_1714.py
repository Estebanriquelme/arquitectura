# Generated by Django 3.2.9 on 2021-11-28 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turismo', '0004_alter_reserva_estado_reserva'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicioextra',
            old_name='precio_depto',
            new_name='precio_serv',
        ),
        migrations.RemoveField(
            model_name='transporte',
            name='precio_depto',
        ),
    ]