from django.shortcuts import render
from django.views import View

from .models import Currency
from .forms import ConvertForm


class FormView(View):
    form_class = ConvertForm
    initial = {'key': 'value'}
    template_name = 'currency/convert.html'

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():

            from_qty = form['from_currency_qty'].value()
            from_currency_pointer = form['From'].value()
            to_currency_pointer = form['To'].value()

            current_currency = Currency.objects.order_by('-pub_date')[:1]\
                .values(from_currency_pointer, to_currency_pointer)
            cost_from = current_currency[0][from_currency_pointer]
            cost_to = current_currency[0][to_currency_pointer]

            to_qty = cost_to * int(from_qty)/cost_from
            to_qty = round(to_qty, 2)

            data = {
                    'from_currency_qty': from_qty,
                    'to_currency_qty': to_qty,
                    'From': form['From'].value(),
                    'To': form['To'].value(),
                    }
            form = ConvertForm(data)

            return render(request, self.template_name, {'form': form})

        return render(request, self.template_name, {'form': form})
