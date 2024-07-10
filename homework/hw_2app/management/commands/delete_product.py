from django.core.management.base import BaseCommand
from hw_2app.models import Product, Order, Client


class Command(BaseCommand):
    help = 'Delete product by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        product = Product.objects.filter(pk=pk).first()
        if product is not None:
            product.delete()
        self.stdout.write(f'Товар №{pk} удален')