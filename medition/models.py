from django.db import models

class Meditions(models.Model):
    MeditionId = models.AutoField(primary_key=True)
    Ph = models.FloatField(max_length=10)
    Voltage = models.FloatField(max_length=10)
    Current = models.FloatField(max_length=20)
