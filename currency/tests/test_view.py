from django.test import TestCase
from django.test import Client
from currency.models import Currency
from datetime import datetime


class SimpleTest(TestCase):
    def setUp(self):
        Currency.objects.create(usd_cost=1.0, euro_cost=2.0, czk_cost=40.0, pln_cost=50.0, pub_date=datetime.today())
        self.client = Client()

    def test_get(self):
        response = self.client.get('/currency/')
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        """
        test post request with all possible values, calculate answer and test response values
        """
        fields = ['usd_cost', 'euro_cost', 'czk_cost', 'pln_cost']
        qty = [100, 999, 3.5, 938756]
        # for every input currency
        for fr in fields:
            # for every output currency
            for to in fields:
                # for every input quantity
                for fr_q in qty:
                        data = {
                            'from_currency_qty': fr_q,
                            'From': fr,
                            'To': to
                        }
                        # take costs from db
                        curr_costs = Currency.objects.order_by('-pub_date')[:1].values(fr, to)
                        response = self.client.post('/currency/', data)

                        cost_fr = curr_costs[0][fr]
                        cost_to = curr_costs[0][to]
                        # input quantity remains as in the request
                        qty_fr = fr_q
                        calculated = cost_to * float(qty_fr) / cost_fr
                        calculated = round(calculated, 2)

                        self.assertEqual(response.status_code, 200)
                        # currencies keys remains as in the request
                        self.assertEqual(response.context['form']['From'].value(), fr)
                        self.assertEqual(response.context['form']['To'].value(), to)
                        # key 'from_currency_qty' remains as in the request
                        self.assertAlmostEqual(float(response.context['form']['from_currency_qty'].value()), fr_q)
                        self.assertAlmostEqual(float(response.context['form']['to_currency_qty'].value()), calculated)
