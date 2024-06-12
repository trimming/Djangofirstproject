from django.core.management.base import BaseCommand
from hw_2app.models import Product

class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **options):

        product = Product(
            name='Ball',
            desc='Ball for ping-pong.',
            price=150.00,
            quantity=5,
            add_date='2023-10-24'
        )

        product.save()
        self.stdout.write(f'Товар {product.name} добавлен.')