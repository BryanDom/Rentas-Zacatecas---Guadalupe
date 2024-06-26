# Generated by Django 4.1.6 on 2023-11-13 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0004_delete_favorito'),
        ('Propiedades', '0010_alter_colonia_municipio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('resena_id', models.AutoField(primary_key=True,
                                               serialize=False)),
                ('descripcion', models.TextField(max_length=500)),
                ('calificacion', models.IntegerField(
                    choices=[('', 'No estrellas'),
                             (1, 'Una Estrella'),
                             (2, 'Dos Estrellas'),
                             (3, 'Tres Estrellas'),
                             (4, 'Cuatro Estrellas'),
                             (5, 'Cinco Estrellas')])),
                ('fecha', models.DateField(auto_now_add=True)),
                ('estudiante', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='resenas_estudiante',
                    to='perfiles.estudiante',
                    verbose_name='Estudiante')),
                ('propiedad', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='resenas_propiedad',
                    to='Propiedades.propiedad',
                    verbose_name='Propiedad')),
            ],
        ),
    ]
