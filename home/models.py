# from django.db import models
# from contacts.models import Realtors
#
# class Property(models.Model):
#     propertyId = models.AutoField(primary_key=True)
#     added = models.DateField()
#     address = models.CharField(max_length=255)
#     country = models.charfield(max_length=255)
#     zipCode = models.CharField(max_length=255)
#     rooms = models.IntegerField()
#     size = models.IntegerField()
#     price = models.IntegerField()
#     description = models.CharField(max_length=255)
#     realtId = models.ForeignKey(Realtors, on_delete=models.CASCADE)
#
#
# class PropImages(models.Model):
#     id = models.AutoField(primary_key=True)
#     propImgUrl = models.CharField(max_length=1024)
#     propertyId = models.ForeignKey(Property, on_delete=models.CASCADE)