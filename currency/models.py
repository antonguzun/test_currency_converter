from django.db import models


class Currency(models.Model):
    usd_cost = models.FloatField()
    euro_cost = models.FloatField()
    czk_cost = models.FloatField()
    pln_cost = models.FloatField()

    pub_date = models.DateField('last update')

    def __str__(self):
        return str(self.pub_date)
