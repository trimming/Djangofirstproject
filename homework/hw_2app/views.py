import logging
from datetime import datetime, timedelta
import pytz
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from .forms import ImageForm, ProductFormForAdd, ProductForm
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


def update_product(request):
    message = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            form_data = form.cleaned_data
            product = form_data['product']
            product.desc = form_data['desc']
            product.price = form_data['price']
            product.quantity = form_data['quantity']
            product.add_date = form_data['add_date']
            product.save()
            message = 'Товар изменен'
            # return redirect('display_product')
    else:
        form = ProductForm()
    return render(request, 'hw_2app/product_form.html', {'form': form, 'message': message, 'btn_text': 'Изменить'})


def upload_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            return redirect('display_product')
    else:
        form = ImageForm()
    return render(request, 'hw_2app/upload_img.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductFormForAdd(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            product = Product.objects.create(name=form_data['name'],
                                   desc=form_data['desc'],
                                   price=form_data['price'],
                                   quantity=form_data['quantity'],
                                   add_date=form_data['add_date'],
                                   )
            product.save()
            return redirect('upload_img')
    else:
        form = ProductFormForAdd()
    return render(request, 'hw_2app/product_form.html', {'form': form, 'btn_text': 'Добавить'})


def display_product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'title': 'Все товары',
            'products': products,
        }
        return render(request, 'hw_2app/display_product.html', context)
