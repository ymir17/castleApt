from django.db import models


class Accounts(models.Model):
    accountId = models.AutoField(primary_key=True)
    lastName = models.CharField(max_length=32)
    firstName = models.CharField(max_length=32)
    phoneNo = models.IntegerField()
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=255)


class Users(models.Model):
    accountId = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipCode = models.IntegerField()
    country = models.CharField(max_length=32)

