# Generated by Django 4.2.1 on 2023-10-07 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Propiedades', '0006_remove_imagenpropiedad_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                                           primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('municipio', models.ForeignKey(
                    on_delete=django.db.models.deletion.DO_NOTHING,
                    to='Propiedades.municipio', verbose_name='Municipio')),
            ],
        ),
    ]
