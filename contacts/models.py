from django.db import models
from signup.models import Accounts


class RealtorImages(models.Model):
    realtImgId = models.AutoField(primary_key=True)
    realtImgUrl = models.CharField(1024)


class Realtors(models.Model):
    realtId = models.AutoField(primary_key=True)
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE())
    description = models.CharField(max_length=1024)
    realtImgId = models.ForeignKey(RealtorImages, on_delete=models.CASCADE())
