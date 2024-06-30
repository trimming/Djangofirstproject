import datetime
import random
from random import choices
from django.core.management.base import BaseCommand
from myapp3.models import Author, Article

LOREM = "Lorem ipsum dolor sit amet, consectetur adipisicingelit. " \
        "Accusamus accusantium aut beatae consequaturconsequuntur cumque, delectus et illo iste maxime " \
        "nihil non nostrum odio officia, perferendis placeatquasi quibusdam quisquam quod sunt " \
        "tempore temporibus ut voluptatum? A aliquam culpaducimus, eaque eum illo mollitia nemo " \
        "tempore unde vero! Blanditiis deleniti ex hic,laboriosam maiores odit officia praesentium " \
        "quae quisquam ratione, reiciendis, veniam. Accusantiumassumenda consectetur consequatur " \
        "consequuntur corporis dignissimos ducimus eius est eumexpedita illo in, inventore " \
        "ipsum iusto maiores minus mollitia necessitatibus nequenisi optio quasi quo quod, " \
        "quos rem repellendus temporibus totam unde vel velitvero vitae voluptates."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Name_{i}',
                            last_name=f'LastName_{i}',
                            email=f'mail{i}@mail.ru',
                            bio=f'bio{i + i}',
                            birthday=datetime.datetime.now())
            author.save()
            for j in range(1, count + 1):
                article = Article(
                    title=f'Title-{j}',
                    text=" ".join(choices(text, k=64)),
                    author=author,
                    category=f'Some category_{i}',
                    is_published=random.choice([True, False])
                )
                article.save()
