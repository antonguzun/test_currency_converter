from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Currency_USD, Currency_Czk, Currency_Euro, Currency_Pln


def index(request):
    current_currency = Currency_USD.objects.order_by('-pub_date')
    context = {'current_currency': current_currency}
    for i in current_currency:
        print(i.id)
        print(i.name)
        print(i.cost)
        print(i.pub_date)
        print('ok')
    print(context)
    return render(request, 'currency/index.html', context)


def detail(request, currency_data):
    return HttpResponse("You're looking at currency %s." % currency_data)


