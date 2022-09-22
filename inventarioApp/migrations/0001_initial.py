# Generated by Django 4.1.1 on 2022-09-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('edad', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_proveedor', models.CharField(max_length=100)),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('cantidad_productos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.PositiveBigIntegerField()),
                ('fecha_compra', models.DateField()),
                ('producto', models.CharField(max_length=100)),
                ('nombre_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventarioApp.cliente')),
            ],
        ),
    ]
