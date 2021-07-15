# Generated by Django 3.2.5 on 2021-07-14 19:57

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
                ('release_date', models.IntegerField()),
                ('engine_volume', models.FloatField()),
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
            name='CarEngine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
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
            name='SteeringWheel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CarPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_price', models.IntegerField(default=0)),
                ('car_location', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=24)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.car')),
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
            name='brand',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.carbrand'),
        ),
        migrations.AddField(
            model_name='car',
            name='car_engine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.carengine'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.carmodel'),
        ),
        migrations.AddField(
            model_name='car',
            name='steering_wheel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.steeringwheel'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CarRentApp.transmissiontype'),
        ),
    ]