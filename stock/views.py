from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from stock.models import Stock


def stock_list(request):
    stocks = Stock.objects.all()
    context = {
        'stocks': stocks,
    }
    return render(request, 'stocks.html', context)
