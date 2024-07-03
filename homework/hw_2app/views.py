import logging
from datetime import datetime, timedelta
import pytz
from django.shortcuts import render
from .models import Product, Client, Order

logger = logging.getLogger(__name__)

utc = pytz.UTC

def home(request):
    logger.info("Index page accessed")
    context = {'title': 'Главная страница'}
    return render(request, 'hw_2app/index.html', context)


def get_orders(request, client_id: int):
    client = Client.objects.filter(id=client_id).first()
    orders = Order.objects.filter(client=client)
    orders_dict = {}
    for order in orders:
        products = Order.objects.get(id=order.id).product.all()
        orders_dict[order] = products
    context = {
        'title': 'Orders',
        'orders': orders_dict,
        'client_name': client.name,

    }
    return render(request, 'hw_2app/orders.html', context)


def sort_orders_by_period(request, client_id: int, period: int):
    client = Client.objects.filter(id=client_id).first()
    orders = Order.objects.filter(client=client)
    orders_dict = {}
    for order in orders:
        now = utc.localize(datetime.now())
        find_period = now - timedelta(days=period)
        print(find_period)
        print(now)
        products = Order.objects.get(id=order.id).product.all()
        if order.order_date >= find_period:
            orders_dict[order] = products
    context = {
        'title': 'Sort orders',
        'orders': orders_dict,
        'client_name': client.name,
        'period': period,
    }
    return render(request, 'hw_2app/sortorders.html', context)