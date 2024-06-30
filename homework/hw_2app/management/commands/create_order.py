import datetime

from django.core.management.base import BaseCommand
from hw_2app.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create order'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')
        parser.add_argument('product_id', type=int, help='Client ID')

    def handle(self, *args, **options):
        client_id = options.get('client_id')
        product_id = options.get('product_id')
        product = Product.objects.get(pk=product_id)
        order = Order(
            client=Client.objects.get(pk=client_id),
            total_price=product.price * product.quantity,
            order_date=datetime.datetime.now()
        )

        order.save()
        order.product.set([product])

        self.stdout.write(f'Заказ №{order.id} создан.')
