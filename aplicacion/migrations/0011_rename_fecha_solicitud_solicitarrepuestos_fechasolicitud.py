# Generated by Django 4.2.9 on 2024-03-01 22:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0010_solicitarrepuestos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='solicitarrepuestos',
            old_name='fecha_solicitud',
            new_name='fechasolicitud',
        ),
    ]
