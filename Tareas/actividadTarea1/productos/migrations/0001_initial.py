# Generated by Django 4.2.2 on 2023-06-23 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=300, verbose_name='Nombre')),
                ('descripcion', models.CharField(default='', max_length=300, verbose_name='Descripcion')),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio')),
                ('fecha_registro', models.CharField(default='', max_length=300, verbose_name='Fecha de registro')),
                ('estatus', models.BooleanField(default=False, verbose_name='Estatus')),
            ],
        ),
    ]
