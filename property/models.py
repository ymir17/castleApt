from django.db import models
from contacts.models import Realtors


class Properties(models.Model):
    propertyId = models.AutoField(auto_created=True, primary_key=True)
    added = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zipCode = models.CharField(max_length=255)
    rooms = models.IntegerField()
    size = models.FloatField()
    price = models.FloatField()
    description = models.CharField(max_length=32)
    realtId = models.ForeignKey(Realtors, on_delete=models.CASCADE)


class PropImages(models.Model):
    propertyId = models.ForeignKey(Properties, on_delete=models.CASCADE)
    propImgUrl = models.CharField(max_length=1024)

