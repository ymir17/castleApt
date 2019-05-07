from django.db import models
from contacts.models import Realtors


class PropImages(models.Model):
    imgId = models.AutoField(primary_key=True)
    propImgUrl = models.CharField(max_length=1024)


class Properties(models.Model):
    added = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zipCode = models.IntegerField()
    rooms = models.IntegerField()
    size = models.FloatField()
    price = models.FloatField()
    imgId = models.ForeignKey(PropImages, on_delete=models.CASCADE)
    realtId = models.ForeignKey(Realtors, on_delete=models.CASCADE)