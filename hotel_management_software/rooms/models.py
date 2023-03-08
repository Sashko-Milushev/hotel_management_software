from django.core import validators
from django.db import models


class Room(models.Model):
    ROOM_MIN_CAPACITY = 1
    ROOM_MAX_CAPACITY = 6

    ROOM_MAX_LEN = 4
    ROOM_MIN_LEN = 1

    number = models.CharField(
        max_length=ROOM_MAX_LEN,
        validators=[validators.MinLengthValidator(ROOM_MIN_LEN)],
        unique=True,
        blank=False,
        null=False

    )

    capacity = models.IntegerField(
        validators=[validators.MinValueValidator(ROOM_MIN_CAPACITY),
                    validators.MaxValueValidator(ROOM_MAX_CAPACITY), ],

        blank=False,
        null=False
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        editable=True,
        blank=False,
        null=False
    )
