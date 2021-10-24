from django.db import models


# Create your models here.


class Rnuma(models.Model):
    rnumber = models.PositiveIntegerField(),
    name = models.CharField(max_length=120),
    address = models.CharField(max_length=500),
    pincode = models.PositiveIntegerField(),
    rtype = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.rnumber} for {self.name}"
