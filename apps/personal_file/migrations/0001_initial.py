# Generated by Django 4.2.8 on 2024-01-13 20:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
                ('predecessor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personal_file.area', verbose_name='Predecesor')),
                ('sucursal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.organization', verbose_name='Sucursal')),
            ],
            options={
                'verbose_name': 'Area',
                'verbose_name_plural': 'Areas',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Sueldo')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('QR', models.ImageField(blank=True, null=True, upload_to='qrcodes/', verbose_name='QR')),
                ('firts_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='empleado', verbose_name='Foto')),
                ('dni', models.CharField(max_length=50, verbose_name='Dni')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono')),
                ('email', models.CharField(max_length=100, verbose_name='Correo')),
                ('direction', models.CharField(max_length=100, verbose_name='Dirección')),
                ('latitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Latitud')),
                ('longitude', models.CharField(blank=True, max_length=100, null=True, verbose_name='Longitud')),
                ('date_admission', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha Ingreso')),
                ('employee_class', models.IntegerField(choices=[(1, 'Nombramiento'), (2, 'Contratado'), (3, 'Jubilado')], default=2, verbose_name='Clase Empleado')),
                ('number_iess', models.CharField(blank=True, max_length=50, null=True, verbose_name='Numero Iess')),
                ('date_membership', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Iess')),
                ('sueldo', models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Sueldo')),
                ('rol', models.BooleanField(default=True, verbose_name='Pago Rol')),
                ('frequency_rol', models.IntegerField(blank=True, choices=[(1, 'Mensual'), (2, 'Quincenal'), (3, 'Semanal')], default=2, null=True, verbose_name='Frecuencia Rol')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personal_file.area', verbose_name='Area')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personal_file.category', verbose_name='Categoria')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.city', verbose_name='Ciudad')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.country', verbose_name='Pais')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='KinshipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('kinship', models.CharField(max_length=100, unique=True, verbose_name='Parentesco')),
                ('age_limit', models.IntegerField(default=18, verbose_name='Edad Limite')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Parentesco',
                'verbose_name_plural': ' Parentescos',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('estado_civil', models.CharField(max_length=50, unique=True, verbose_name='Estado civil')),
                ('state', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Estado civil',
                'verbose_name_plural': 'Estado civil',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('profile', models.TextField(verbose_name='Perfil')),
                ('studies', models.TextField(max_length=200, verbose_name='Estudios')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='TypeArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Tipo Area',
                'verbose_name_plural': 'Tipo Areas',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='TypeContract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Tipo Contrato',
                'verbose_name_plural': 'Tipo Contratos',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='TypeEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Descripcion')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Tipo Empleado',
                'verbose_name_plural': 'Tipo Empelados',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='TypeRegime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Tipo Regimen',
                'verbose_name_plural': 'Tipo Regimens',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Medicaldata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('tipo_sangre', models.CharField(max_length=10, verbose_name='Tipo de sangre')),
                ('alergias', models.TextField(blank=True, verbose_name='Alergias')),
                ('enfermedades', models.TextField(blank=True, verbose_name='Enfermedades')),
                ('peso', models.CharField(max_length=10, verbose_name='Peso(kg)')),
                ('altura', models.CharField(max_length=10, verbose_name='Altura(m)')),
                ('Ultima_revision', models.DateField(default=django.utils.timezone.now, verbose_name='Ultima revision')),
                ('discapacidad', models.BooleanField(default=False, verbose_name='Discapacidad')),
                ('des_discapacidad', models.TextField(blank=True, verbose_name='descripcion de Discapacidad')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_file.employee', verbose_name='Empleado')),
            ],
            options={
                'verbose_name': 'Dato Medico',
                'verbose_name_plural': 'Dato Medicos',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='marital_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personal_file.maritalstatus', verbose_name='Estado Civil'),
        ),
        migrations.AddField(
            model_name='employee',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personal_file.post', verbose_name='Cargo'),
        ),
        migrations.AddField(
            model_name='employee',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.organization', verbose_name='Sucursal'),
        ),
        migrations.AddField(
            model_name='employee',
            name='type_contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personal_file.typecontract', verbose_name='Tipo Contrato'),
        ),
        migrations.AddField(
            model_name='employee',
            name='type_employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personal_file.typeemployee', verbose_name='Tipo Empleado'),
        ),
        migrations.AddField(
            model_name='employee',
            name='type_regime',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='personal_file.typeregime', verbose_name='Tipo Regimen'),
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('lastname', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('fecha_nacimiento', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha de nacimiento')),
                ('image', models.ImageField(blank=True, max_length=500, null=True, upload_to='dependents', verbose_name='Foto')),
                ('direction', models.CharField(max_length=100, verbose_name='Dirección')),
                ('phone', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('cedula', models.CharField(max_length=50, unique=True, verbose_name='Cedula')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.city', verbose_name='Ciudad')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.country', verbose_name='Pais')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_file.employee', verbose_name='Empleado Responsable')),
                ('kinship', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personal_file.kinshiptype', verbose_name='Parentesco')),
                ('marital_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personal_file.maritalstatus', verbose_name='Estado Civil')),
            ],
            options={
                'verbose_name': 'Carga Familiar',
                'verbose_name_plural': 'Cargas Familiares',
                'ordering': ('-id',),
            },
        ),
        migrations.AddField(
            model_name='area',
            name='type_area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='personal_file.typearea', verbose_name='type_area'),
        ),
    ]