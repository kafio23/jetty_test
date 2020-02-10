from django.db import models


class Driver(models.Model):
    driver_id = models.IntegerField(null=False, unique=True)
    email = models.CharField(max_length=30, null=False, unique=True)
    auth_token = models.CharField(max_length=50, null=False)
