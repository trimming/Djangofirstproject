from django.core.management.base import BaseCommand
from hw_2app.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **options):

        client = Client(
            name='Alex',
            email='alex@example.ru',
            phone_number=88009009001,
            address='Moscow, Arbat street, 56',
            login_date='2023-12-23'
        )
        client.save()
        self.stdout.write(f'Клиент {client.name} зарегистрирован.')