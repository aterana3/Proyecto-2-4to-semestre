# Generated by Django 4.2.8 on 2024-01-22 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='login',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='login'),
        ),
    ]
