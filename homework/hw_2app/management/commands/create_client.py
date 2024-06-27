from django.core.management.base import BaseCommand
from hw_2app.models import Client


class Command(BaseCommand):
    help = 'Create client'

    def handle(self, *args, **options):

        client = Client(
            name='Maksim',
            email='maksim@example.ru',
            phone_number=78009009001,
            address='Anapa, Lenina street, 6',
            login_date='2023-06-20'
        )
        client.save()
        self.stdout.write(f'Клиент {client.name} зарегистрирован.')