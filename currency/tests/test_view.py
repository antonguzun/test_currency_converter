from django.test import TestCase
import unittest
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_get(self):
        # Issue a GET request.
        response = self.client.get('/currency/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        # Check that the response is 200 OK for every pair of currencies.
        from_arr = ['usd_cost', 'euro_cost', 'czk_cost', 'pln_cost']
        to_arr = from_arr
        qty_arr = ['0.1', '10', '102', '2323', '9999', '9821023']
        for i in from_arr:
            for j in to_arr:
                for qty in qty_arr:
                    response = self.client.post('/currency/',
                                                {'From': i, 'To': j, 'from_currency_qty': qty})
                    self.assertEqual(response.status_code, 200)
        print(response.content)