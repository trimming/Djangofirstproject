from django.core.management.base import BaseCommand
from hw_2app.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create order'

    def handle(self, *args, **options):
        order = Order(
            client=Client.objects.get(pk=1),
            product=Product.objects.set(name__iexact='ball'),
            total_price=150,
            order_date='2023-12-25'
        )
        order.save()
        self.stdout.write(f'Заказ №{order.id} создан.')
