import datetime

from django.db import models
from django.utils import timezone


class Currency(models.Model):
    usd_cost = models.FloatField()
    euro_cost = models.FloatField()
    czk_cost = models.FloatField()
    pln_cost = models.FloatField()

    pub_date = models.DateField('last update')

    def __str__(self):
        return str(self.pub_date)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



