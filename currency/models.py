import datetime

from django.db import models
from django.utils import timezone


class Currency_USD(models.Model):
    name = models.CharField(max_length=10)
    cost = models.FloatField()
    pub_date = models.DateField('last update')
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Currency_Pln(models.Model):
    usd = models.ForeignKey(Currency_USD, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    cost = models.FloatField()
    def __str__(self):
        return self.name


class Currency_Czk(models.Model):
    usd = models.ForeignKey(Currency_USD, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    cost = models.FloatField()
    def __str__(self):
        return self.name


class Currency_Euro(models.Model):
    usd = models.ForeignKey(Currency_USD, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    cost = models.FloatField()
    def __str__(self):
        return self.name



