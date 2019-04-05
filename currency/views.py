from django.shortcuts import render
from django.views import View

from .models import Currency
from .forms import ConvertForm


def convert(cost_fr, cost_to, qty):
    """
    simple math fun convert from from_curr (quantity_from_curr=qty) into to_curr
    :return: float quantity_to_curr
    """
    quantity = cost_to * float(qty)/cost_fr
    quantity = round(quantity, 2)
    return quantity


class FormView(View):
    form_class = ConvertForm
    initial = {'key': 'value'}
    template_name = 'currency/convert.html'

    def get(self, request):
        """
        just render form
        :return: rendered form
        """
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        """
        put calculated data into new form and render that
        :return: rendered form
        """
        form = self.form_class(request.POST)
        if form.is_valid():

            # take old data from from
            from_qty = form['from_currency_qty'].value()
            from_currency_pointer = form['From'].value()
            to_currency_pointer = form['To'].value()

            # take currencies courses from db
            current_currency = Currency.objects.order_by('-pub_date')[:1]\
                .values(from_currency_pointer, to_currency_pointer)
            current_currency = current_currency[0]
            cost_from = current_currency[from_currency_pointer]
            cost_to = current_currency[to_currency_pointer]

            # calculate convert
            calculated_qty = convert(cost_fr=cost_from, qty=from_qty, cost_to=cost_to)
            # currencies keys and key 'from_currency_qty' remains as in the request
            data = {
                    'from_currency_qty': from_qty,
                    'to_currency_qty': calculated_qty,
                    'From': form['From'].value(),
                    'To': form['To'].value(),
                    }
            # put into form (actually make new form)
            form = ConvertForm(data)
            return render(request, self.template_name, {'form': form})

        # if form is not valid just render clean form
        return render(request, self.template_name, {'form': form})
