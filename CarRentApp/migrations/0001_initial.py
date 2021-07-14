# Generated by Django 3.2.5 on 2021-07-05 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transmission_type', models.CharField(choices=[('AUTOMATIC', 'Automatic'), ('MECHANICAL', 'Mechanical')], max_length=64)),
                ('steering_wheel', models.CharField(choices=[('LEFT', 'Left'), ('RIGHT', 'Right')], max_length=64)),
                ('car_engine', models.CharField(choices=[('OIL', 'Oil'), ('DIESEL', 'Diesel'), ('GAS', 'Gas'), ('HYBRID', 'Hybrid'), ('ELECTRIC', 'Electric')], max_length=64)),
                ('release_date', models.IntegerField()),
                ('engine_volume', models.IntegerField()),
                ('car_kilometrage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_location', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=24)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.carbrand')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.cartype')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.carmodel'),
        ),
    ]
