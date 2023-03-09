from django.core import validators
from django.db import models

from hotel_management_software.rooms.models import Room


class Reservation(models.Model):
    CUSTOMER_MAX_LEN = 50
    CUSTOMER_MIN_LEN = 5
    CUSTOMER_PHONE_MAX_LEN = 20

    customer_name = models.CharField(
        max_length=CUSTOMER_MAX_LEN,
        validators=validators.MinValueValidator(CUSTOMER_MIN_LEN),
        blank=False,
        null=False
    )
    count_of_accommodated_persons = models.IntegerField()
    start_date = models.DateTimeField(
        blank=False,
        null=False
    )
    end_date = models.DateTimeField(
        blank=False,
        null=False
    )
    customer_phone = models.CharField(
        max_length=CUSTOMER_PHONE_MAX_LEN,
        blank=False,
        null=False
    )
    occupied_rooms = models.ManyToManyField(
        Room
    )
