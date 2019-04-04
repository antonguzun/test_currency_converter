from django import forms


class ConvertForm(forms.Form):
    CHOICES = (('euro_cost', 'EUR'),
               ('usd_cost', 'USD'),
               ('czk_cost', 'CZK'),
               ('pln_cost', 'PLN'))
    From = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    To = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    from_currency_qty = forms.IntegerField()
    to_currency_qty = forms.FloatField(required=False)
