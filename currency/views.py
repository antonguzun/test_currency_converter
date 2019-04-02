from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Currency


def index(request):
    current_currency = Currency.objects.order_by('-pub_date')
    context = {'current_currency': current_currency}
    for i in current_currency:
        print('id: ', i.id)
        print('USD: ', i.usd_cost)
        print('EUR: ', i.euro_cost)
        print('CZK: ', i.czk_cost)
        print('PLN: ', i.pln_cost)
    print(context)
    return render(request, 'currency/index.html', context)


def detail(request, currency_data):
    return HttpResponse("You're looking at currency %s." % currency_data)


