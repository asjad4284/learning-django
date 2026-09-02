from django.db import models

class Logger(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    time_log=models.TimeField()