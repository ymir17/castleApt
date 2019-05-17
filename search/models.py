from django.db import models
from search.choices import *

# Create your models here.

class prop(models.Model):
    order = models.IntegerField(choices=ORDER_BY, default=1)