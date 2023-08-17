# Generated by Django 4.2.4 on 2023-08-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_tickets_fechaactualizacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='fechaAtencion',
            field=models.DateField(default='', verbose_name='Fecha de atencion'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='fechaTerminacionFinal',
            field=models.DateField(default='', verbose_name='Fecha de finalizacion real'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='fechaTerminacionPrevista',
            field=models.DateField(default='', verbose_name='Fecha de finalizacion programada'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='statusTicket',
            field=models.CharField(default='', max_length=2, verbose_name='Status ticket'),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='usuarioEncargado',
            field=models.CharField(default='', max_length=50, verbose_name='Usuario encargado'),
        ),
    ]
