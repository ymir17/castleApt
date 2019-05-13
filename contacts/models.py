from django.db import models
from signup.models import Accounts


class RealtorImages(models.Model):
    realtImgId = models.AutoField(auto_created=True, primary_key=True)
    realtImgUrl = models.CharField(max_length=1024)
    def __str__(self):
        return self.realtImgUrl



class Realtors(models.Model):
    #name = models.CharField(max_length=255)
    realtId = models.AutoField(auto_created=True, primary_key=True)
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    realtImgId = models.ForeignKey(RealtorImages, on_delete=models.CASCADE)
