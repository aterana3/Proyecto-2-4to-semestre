# Generated by Django 4.2.8 on 2024-01-13 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal_file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarVacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('anio', models.IntegerField(unique=True)),
                ('num_empleados', models.IntegerField()),
                ('status', models.IntegerField(choices=[(1, 'Generado'), (2, 'Pendientes Procesar'), (3, 'Procesado')])),
            ],
            options={
                'verbose_name': 'Calendario Vacacion',
                'verbose_name_plural': 'Calendario Vacaciones',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Vacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('mes', models.IntegerField()),
                ('desde', models.DateField(verbose_name='Fecha desde')),
                ('hasta', models.DateField(verbose_name='Fecha Hasta')),
                ('dias_menos_por_permiso', models.IntegerField(default=0)),
                ('dias_vacacion', models.IntegerField()),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Sueldo')),
                ('status', models.IntegerField(choices=[(1, 'Sin tomar'), (2, 'Gozado')])),
                ('calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_vacation.calendarvacation')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_file.employee')),
            ],
            options={
                'verbose_name': 'Vacacion',
                'verbose_name_plural': 'Vacaciones',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='ChangeVacation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('fecha_pedido', models.DateField(verbose_name='Fecha Pedido')),
                ('mes', models.IntegerField()),
                ('reason', models.CharField(blank=True, max_length=200, null=True, verbose_name='Reason')),
                ('approved', models.BooleanField(default=False, verbose_name='Aprobado')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_file.employee')),
            ],
            options={
                'verbose_name': 'Cambio Vacacion',
                'verbose_name_plural': 'Cambio Vacaciones',
                'ordering': ('-id',),
            },
        ),
    ]
