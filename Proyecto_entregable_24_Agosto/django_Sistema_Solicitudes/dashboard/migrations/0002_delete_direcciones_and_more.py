# Generated by Django 4.2.4 on 2023-08-19 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='direcciones',
        ),
        migrations.RenameField(
            model_name='archivos',
            old_name='folioTicket',
            new_name='idTicket',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='archivosAdjuntos',
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='folioTicket',
        ),
    ]
