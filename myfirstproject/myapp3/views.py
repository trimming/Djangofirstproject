import random

from django.shortcuts import render
from django.http import HttpResponse
import logging

# Create your views here.
logger = logging.getLogger(__name__)


def home(request):
    logger.info("Index page accessed")
    context = {'title': 'Главная страница'}
    return render(request, 'myapp3/index.html', context)


def get_info_about(request):
    logger.info("About page accessed")
    context = {'name': 'Алексей',
               'title': 'Обо мне'}
    return render(request, 'myapp3/about.html', context)


def flip_coin(request, count: int):
    logger.info("Coin page accessed")
    res = [random.choice(["Орёл", "Решка"]) for _ in range(count)]
    context = {
        'title': 'Flip coin',
        'content': res,
    }
    return render(request, 'myapp3/games.html', context)


def flip_cube(request, count: int):
    logger.info("Cube page accessed")
    res = [random.randint(1, 6) for _ in range(count)]
    context = {
        'title': 'Random roll',
        'content': res
    }
    return render(request, 'myapp3/games.html', context)


def get_random_number(request, count: int):
    logger.info("Number page accessed")
    result = [random.randint(1, 100) for _ in range(count)]
    context = {
        'title': 'Random number',
        'content': result
    }
    return render(request, 'myapp3/games.html', context)
