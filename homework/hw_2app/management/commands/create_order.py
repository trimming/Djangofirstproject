from django.core.management.base import BaseCommand
from hw_2app.models import Order, Client, Product


class Command(BaseCommand):
    help = 'Create order'

    def handle(self, *args, **options):
        prod_id = Product.objects.get(pk=3)
        order = Order(
            client=Client.objects.get(pk=2),
            total_price=prod_id.price * prod_id.quantity,
            order_date='2024-06-15'
        )

        order.save()
        order.product.set([prod_id])

        self.stdout.write(f'Заказ №{order.id} создан.')
