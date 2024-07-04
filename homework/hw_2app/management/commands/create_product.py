import datetime

from django.core.management.base import BaseCommand
from hw_2app.models import Product


class Command(BaseCommand):
    help = 'Create product'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('desc', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('quan', type=str, help='Product quantity')

    def handle(self, *args, **options):
        name = options.get('name')
        desc = options.get('desc')
        price = options.get('price')
        quantity = options.get('quan')
        product = Product(
            name=name,
            desc=desc,
            price=price,
            quantity=quantity,
            add_date=datetime.datetime.now()
        )

        product.save()
        self.stdout.write(f'Товар {product.name} добавлен.')
