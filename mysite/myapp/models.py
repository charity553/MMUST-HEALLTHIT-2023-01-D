import uuid
from django.db import models
from uuid import UUID


# Create your models here.
# create a class for registration
# Creating the fields attributes of our class person
class Person(models.Model):
    # a unique identifier that is human readable
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    area_name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)


# create a class for our triage which will capture vitals
class Triage(models.Model):
    # add the Triage fields
    temperature = models.CharField(max_length=3)
    blood_pressure = models.CharField(max_length=3)
    respiratory_rate = models.CharField(max_length=3)
    pulse_rate = models.CharField(max_length=10)
    weight = models.CharField(max_length=3)
    height = models.CharField(max_length=3)
