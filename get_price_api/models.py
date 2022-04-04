from django.db import models

# Create your models here.
class prices(models.Model):
    start_date = models.CharField(max_length=8)
    end_date = models.CharField(max_length=8)