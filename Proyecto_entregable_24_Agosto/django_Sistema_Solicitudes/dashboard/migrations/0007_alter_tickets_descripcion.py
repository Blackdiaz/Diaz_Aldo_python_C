# Generated by Django 4.2.2 on 2023-08-23 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_tickets_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='descripcion',
            field=models.CharField(default='', max_length=1000, verbose_name='Descripcion'),
        ),
    ]
