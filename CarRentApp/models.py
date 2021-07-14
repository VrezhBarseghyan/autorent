from enum import Enum

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
    model = models.ForeignKey(CarModel, on_delete=models.PROTECT, null=False)
    transmission_type = models.ForeignKey(TransmissionType, on_delete=models.PROTECT, null=False)
    steering_wheel = models.ForeignKey(SteeringWheel, on_delete=models.PROTECT, null=False)
    car_engine = models.ForeignKey(CarEngine, on_delete=models.PROTECT, null=False)
    release_date = models.IntegerField()
    engine_volume = models.FloatField()
    car_kilometrage = models.IntegerField()

    def __str__(self):
        return self.model.name

class CarPost(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT, null=False)
    car_price = models.IntegerField(default=0)
    car_location = models.CharField(max_length=64)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=24)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car.model.name + self.car.model.brand.name

# class Order(models.Model):
#     pickup_location = models.c