# Generated by Django 3.2.5 on 2021-07-17 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CarRentApp', '0002_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carpost',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CarRentApp.customer'),
        ),
    ]
