# Generated by Django 3.1.1 on 2020-10-30 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=30)),
                ('abreviatura', models.CharField(max_length=10)),
                ('estado', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(verbose_name='Date creation')),
                ('update_date', models.DateTimeField(verbose_name='Date update')),
            ],
        ),
        migrations.CreateModel(
            name='Razas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=30)),
                ('abreviatura', models.CharField(max_length=10)),
                ('estado', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(verbose_name='Date creation')),
                ('update_date', models.DateTimeField(verbose_name='Date update')),
                ('id_tipos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.tipos')),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=30)),
                ('tiene_vacunas', models.BooleanField(default=False)),
                ('estado', models.BooleanField(default=True)),
                ('create_date', models.DateTimeField(verbose_name='Date creation')),
                ('update_date', models.DateTimeField(verbose_name='Date update')),
                ('id_raza', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.razas')),
                ('id_tipos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mascotas.tipos')),
            ],
        ),
    ]
