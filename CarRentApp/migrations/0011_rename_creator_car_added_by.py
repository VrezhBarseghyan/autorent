# Generated by Django 3.2.5 on 2021-07-15 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentApp', '0010_rename_added_by_car_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='creator',
            new_name='added_by',
        ),
    ]