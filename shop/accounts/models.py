from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, null=True, default=None)
    street = models.CharField(max_length=100, null=True, default=None)
    building_number = models.CharField(max_length=5, null=True, default=None)
    flat_number = models.IntegerField(null=True, default=None, blank=True)
    postal_code = models.CharField(max_length=6, null=True, default=None)

    def __str__(self):
        return f'{self.user.username} - {self.street} {self.building_number}'
