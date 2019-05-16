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
    price = models.IntegerField()
    description = models.CharField(max_length=32)
    realtId = models.ForeignKey(Realtors, on_delete=models.CASCADE)
    yearbuilt = models.DateField(null=True)
    bathrooms = models.FloatField(null=True)
    bedrooms = models.IntegerField(null=True)


class PropImages(models.Model):
    propertyId = models.ForeignKey(Properties, on_delete=models.CASCADE)
    propImgUrl = models.CharField(max_length=1024)

    def __str__(self):
        return self.propImgUrl

