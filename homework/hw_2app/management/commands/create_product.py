from django.core.management.base import BaseCommand
from hw_2app.models import Product


class Command(BaseCommand):
    help = 'Create product'

    def handle(self, *args, **options):
        product = Product(
            name='blanket',
            desc='warm blanket',
            price=200.00,
            quantity=2,
            add_date='2023-07-04'
        )

        product.save()
        self.stdout.write(f'Товар {product.name} добавлен.')
