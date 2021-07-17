from enum import Enum
from django.core.validators import RegexValidator
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

import datetime

# Create your models here.




class CarBrand(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name

class CarType(models.Model):
    name = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(unique=True, max_length=64)
    brand = models.ForeignKey(CarBrand, on_delete=models.PROTECT, null=False)
    type = models.ForeignKey(CarType, on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.name

class TransmissionType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class SteeringWheel(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class CarEngine(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.SET_NULL, blank=True, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.PROTECT, null=False)
    transmission_type = models.ForeignKey(TransmissionType, on_delete=models.PROTECT, null=False)
    steering_wheel = models.ForeignKey(SteeringWheel, on_delete=models.PROTECT, null=False)
    car_engine = models.ForeignKey(CarEngine, on_delete=models.PROTECT, null=False)
    release_date = models.IntegerField(validators=[RegexValidator(
        regex='^(19|[2-9][0-9])\d{2}$',
        message = ['Մուտքագրեք իրական թվական բռատ']
    )])
    engine_volume = models.FloatField()
    car_kilometrage = models.IntegerField()
    added_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    photo = models.ImageField(upload_to='cars', null=True, blank=False)

    def __str__(self):
        return self.model.name

class CarPost(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=False)
    car_price = models.IntegerField(default=0)
    car_location = models.CharField(max_length=64)
    added_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=24)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ' ' + self.car.model.brand.name + " " + self.car.model.name + ' ' + str(self.added_by) + ' ' + str(self.creation_date)

class Order(models.Model):
    chosen_car = models.ForeignKey(CarPost, on_delete=models.PROTECT, null=False)
    date = models.DateField()
    pickup_location = models.CharField(max_length=128)

    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=64, null=True)
    email = models.CharField(max_length=64, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name