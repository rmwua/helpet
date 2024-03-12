import shortuuid
from django.contrib.auth.models import User
from django.contrib.postgres import fields as postgres_fields
from django.db import models


def avatar_upload_to(instance, filename):
    return "uploads/avatars/{0}".format(shortuuid.uuid())


class Pet(models.Model):
    name = models.CharField()
    species = models.CharField()
    breed = models.CharField()
    microchip = models.CharField()
    special_needs = postgres_fields.ArrayField(models.CharField(), default=list)
    avatar = models.ImageField(upload_to=avatar_upload_to)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Appointment(models.Model):
    AppointmentTypes = models.TextChoices("AppointmentTypes", ["Vet", "Vaccination"])
    name = models.CharField()
    type = models.CharField(choices=AppointmentTypes.choices)
    date = models.DateTimeField()
    note = models.TextField()
    pet = models.ForeignKey(Pet, related_name='appointments', on_delete=models.CASCADE)


class MedicalHistoryItem(models.Model):
    MedicalHistoryTypes = models.TextChoices("MedicalHistoryTypes", ["Medication", "Vaccination"])
    name = models.CharField()
    type = models.CharField(choices=MedicalHistoryTypes.choices)
    date = models.DateTimeField()
    note = models.TextField()
    pet = models.ForeignKey(Pet, related_name='medical_history_items', on_delete=models.CASCADE)

    class Meta:
        db_table = "pets_medical_history"


class Note(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
