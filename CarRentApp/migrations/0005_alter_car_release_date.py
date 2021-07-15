# Generated by Django 3.2.5 on 2021-07-15 15:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentApp', '0004_alter_car_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='release_date',
            field=models.IntegerField(validators=[django.core.validators.RegexValidator(message=['Մուտքագրեք իրական թվական բռատ'], regex='(19[789]\\d|20[01]\\d')]),
        ),
    ]