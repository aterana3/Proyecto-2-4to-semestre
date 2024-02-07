# Generated by Django 4.2.8 on 2024-01-13 20:52

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('icon', models.CharField(max_length=100, verbose_name='Icono')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('url', models.CharField(max_length=100, unique=True, verbose_name='Url')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='Icono')),
                ('is_active', models.BooleanField(default=True, verbose_name='Es activo')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='security.menu', verbose_name='Menu')),
                ('permissions', models.ManyToManyField(blank=True, to='auth.permission', verbose_name='Permisos')),
            ],
            options={
                'verbose_name': 'Modulo',
                'verbose_name_plural': 'Modulos',
                'ordering': ('-name',),
            },
        ),
        migrations.CreateModel(
            name='GroupModulePermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('update_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.group', verbose_name='Grupo')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='security.module', verbose_name='Modulo')),
                ('permissions', models.ManyToManyField(to='auth.permission')),
            ],
            options={
                'verbose_name': 'Grupo modulo permiso',
                'verbose_name_plural': 'Grupos modulos Permisos',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dni', models.CharField(blank=True, max_length=13, null=True, verbose_name='Cédula o RUC')),
                ('image', models.ImageField(blank=True, max_length=1024, null=True, upload_to='users', verbose_name='Archive image')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('direction', models.CharField(blank=True, max_length=200, null=True, verbose_name='Direccion')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefono')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.organization')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'permissions': (('change_userprofile', 'Cambiar perfil Usuario'), ('change_userpassword', 'Cambiar password Usuario')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]