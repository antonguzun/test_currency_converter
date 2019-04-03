from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render

import json

from .models import Currency


def index(request):
    current_currency = Currency.objects.order_by('-pub_date')[:1].values('id', 'usd_cost', 'euro_cost',
                                                                         'czk_cost', 'pln_cost', 'pub_date')
    context = {'current_currency': current_currency}
    response_obj = [dict(q) for q in current_currency]
    print(type(response_obj))
    print(response_obj)
    json_data = json.dumps(response_obj, indent=4, sort_keys=False, default=str)
    print('json: ', type(json_data), json_data)
    return render(request, 'currency/index.html', context, status=200)


def convert(request):
    #question = get_object_or_404(Currency, pk=question_id)
    try:
        print(request.POST)
        request_data = request.POST
        from_currency = request_data['from_currency']
        to_currency = request_data['to_currency']
        qty = int(request_data['qty_from'])
        #print(from_currency, to_currency, qty)
        current_currency_target = Currency.objects.order_by('-pub_date')[:1].values(from_currency, to_currency, 'pub_date')
        print(current_currency_target[0])
        cost_from = current_currency_target[0][from_currency]
        cost_to = current_currency_target[0][to_currency]
        qty_to_currency = cost_to*qty/cost_from
        context = {'current_currency_target': current_currency_target,
                   'qty_to_currency': qty_to_currency,
                   'qty_from_currency': qty,
                   'from_currency': from_currency,
                   'to_currency': to_currency,
                   }
        print('context', context)
        return render(request, 'currency/index.html', context, status=200)
    except Exception as e:
        # Redisplay the question voting form.
        return render(request, 'currency/index.html', {
            'error_message': str(e),
        })



def detail(request, currency_data):
    return HttpResponse("You're looking at currency %s." % currency_data)
