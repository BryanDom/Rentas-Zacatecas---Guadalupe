# Generated by Django 4.2.1 on 2023-10-20 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0002_arrendador_usuario_estudiante_usuario'),
        ('Propiedades', '0007_municipio_alter_propiedad_descripcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='TelefonoArrendador',
        ),
        migrations.RemoveField(
            model_name='propiedad',
            name='correoArrendador',
        ),
        migrations.RemoveField(
            model_name='propiedad',
            name='nombreArrendador',
        ),
        migrations.AddField(
            model_name='propiedad',
            name='arrendador',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to='perfiles.arrendador', verbose_name='Arrendador'),
            preserve_default=False,
        ),
    ]
