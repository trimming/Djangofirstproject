import datetime

from django import forms

from .models import Product


class ProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Товар')
    desc = forms.CharField(widget=forms.Textarea(), label='Описание')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')
    quantity = forms.IntegerField(label='Количество')
    add_date = forms.DateTimeField(initial=datetime.date.today, label='Дата изменения')


class ImageForm(forms.Form):
    image = forms.ImageField()


class ProductFormForAdd(forms.Form):
    name = forms.CharField(min_length=3, max_length=60, label='Название товара')
    desc = forms.CharField(widget=forms.Textarea(), label='Описание')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')
    quantity = forms.IntegerField(label='Количество')
    add_date = forms.DateTimeField(initial=datetime.date.today, label='Дата изменения')
