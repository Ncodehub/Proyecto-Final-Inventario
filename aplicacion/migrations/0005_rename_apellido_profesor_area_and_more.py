# Generated by Django 4.2.9 on 2024-02-04 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_repuestos_delete_cursos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profesor',
            old_name='apellido',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='nombre',
            new_name='maquina',
        ),
        migrations.RenameField(
            model_name='profesor',
            old_name='profesion',
            new_name='marca',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='email',
        ),
    ]