from django.test import TestCase
from currency.models import Currency
from django.test import Client
from datetime import datetime
from currency.forms import ConvertForm


class FormTest(TestCase):
    def setUp(self):
        Currency.objects.create(usd_cost=1.0, euro_cost=2.0, czk_cost=30, pln_cost=50, pub_date=datetime.today())
        self.client = Client()

    def test_form_valid(self):
        """
        test all possible values is validate for form
        """
        fields = ['usd_cost', 'euro_cost', 'pln_cost', 'czk_cost']
        qty = [100, 9999, 23214]
        # for every input currency
        for fr in fields:
            # for every output currency
            for to in fields:
                # for every input quantity
                for fr_q in qty:
                    # for every output quantity
                    for to_q in qty:
                        data = {
                            'from_currency_qty': str(fr_q),
                            'to_currency_qty': str(to_q),
                            'From': fr,
                            'To': to
                        }
                        form = ConvertForm(data)

                        response = self.client.post('/currency/', data)
                        self.assertEqual(response.status_code, 200)
                        self.assertTrue(form.is_valid())

