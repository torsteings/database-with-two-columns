from django.db import models

# Create your models here.
class Job(models.Model):
    url = models.CharField(max_length=80)
    open_price = models.DecimalField(max_digits=20, decimal_places=15)
