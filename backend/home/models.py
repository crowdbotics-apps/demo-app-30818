from django.conf import settings
from django.db import models


class Member(models.Model):
    "Generated Model"
    first_name = models.CharField(
        max_length=256,
    )
    last_name = models.CharField(
        max_length=256,
    )
    email = models.EmailField(
        max_length=254,
    )
    phone_number = models.IntegerField()
    gender = models.CharField(
        max_length=256,
    )


class Wish(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    product_url = models.URLField()
    status = models.CharField(
        max_length=256,
    )
