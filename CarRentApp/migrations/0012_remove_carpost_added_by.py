# Generated by Django 3.2.5 on 2021-07-15 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentApp', '0011_rename_creator_car_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carpost',
            name='added_by',
        ),
    ]