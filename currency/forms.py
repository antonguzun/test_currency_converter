from django import forms


class ConvertForm(forms.Form):
    """
    form for '/currency/'
    """
    CHOICES = (('euro_cost', 'EUR'),
               ('usd_cost', 'USD'),
               ('czk_cost', 'CZK'),
               ('pln_cost', 'PLN'))
    # currency from convert - HTML select
    From = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    # currency to convert - HTML select
    To = forms.ChoiceField(widget=forms.Select, choices=CHOICES)

    # quantity currency from convert
    from_currency_qty = forms.FloatField()
    # quantity currency by response
    to_currency_qty = forms.FloatField(required=False)
