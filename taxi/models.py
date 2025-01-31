from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.OneToOneField(
        Manufacturer, on_delete=models.CASCADE, unique=True
    )
    driver = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="drivers"
    )


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
