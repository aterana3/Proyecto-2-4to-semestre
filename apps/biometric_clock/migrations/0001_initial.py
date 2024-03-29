# Generated by Django 4.2.8 on 2024-01-13 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal_file', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('descripcion', models.CharField(max_length=200, verbose_name='Jornada')),
                ('dia_desde', models.IntegerField(choices=[(0, 'Lunes'), (1, 'Martes'), (2, 'Miercoles'), (3, 'Jueves'), (4, 'Viernes'), (5, 'Sabado'), (6, 'Domingo')], default=0)),
                ('dia_hasta', models.IntegerField(choices=[(0, 'Lunes'), (1, 'Martes'), (2, 'Miercoles'), (3, 'Jueves'), (4, 'Viernes'), (5, 'Sabado'), (6, 'Domingo')], default=4)),
                ('hora_entrada', models.TimeField()),
                ('hora_salida_lunch', models.TimeField()),
                ('hora_entrada_lunch', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('horas_trabajo', models.IntegerField(default=8, verbose_name='Horas Trabajadas')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MarcadaReloj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('fecha', models.DateField()),
                ('hora_entrada', models.TimeField(blank=True, null=True)),
                ('hora_salida_lunch', models.TimeField(blank=True, null=True)),
                ('hora_entrada_lunch', models.TimeField(blank=True, null=True)),
                ('hora_salida', models.TimeField(blank=True, null=True)),
                ('horas_trabajadas', models.IntegerField(default=0, verbose_name='Horas Trabajadas')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_file.employee')),
                ('jornada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biometric_clock.jornada')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
