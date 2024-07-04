import datetime

from django.core.management.base import BaseCommand
from hw_2app.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Client name')
        parser.add_argument('email', type=str, help='Client email')
        parser.add_argument('phone', type=int, help='Client phone number')
        parser.add_argument('address', type=str, help='Client address')

    def handle(self, *args, **options):
        name = options.get('name')
        email = options.get('email')
        phone = options.get('phone')
        address = options.get('address')
        client = Client(
            name=name,
            email=email,
            phone_number=phone,
            address=address,
            login_date=datetime.datetime.now()
        )
        client.save()
        self.stdout.write(f'Клиент {client.name} зарегистрирован.')