# Generated by Django 4.2.2 on 2023-06-24 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0002_alter_motos_id_alter_producto_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Motos',
            new_name='modelos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
    ]