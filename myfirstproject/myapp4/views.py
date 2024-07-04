import logging

from django.shortcuts import render

# Create your views here.
from .forms import RandomGame
import random

logger = logging.getLogger(__name__)


def flip_coin(request, count: int):
    logger.info("Coin page accessed")
    res = [random.choice(["Орёл", "Решка"]) for _ in range(count)]
    context = {
        'title': 'Flip coin',
        'content': res,
    }
    return render(request, 'myapp4/games.html', context)


def flip_cube(request, count: int):
    logger.info("Cube page accessed")
    res = [random.randint(1, 6) for _ in range(count)]
    context = {
        'title': 'Random roll',
        'content': res
    }
    return render(request, 'myapp4/games.html', context)


def get_random_number(request, count: int):
    logger.info("Number page accessed")
    result = [random.randint(1, 100) for _ in range(count)]
    context = {
        'title': 'Random number',
        'content': result
    }
    return render(request, 'myapp4/games.html', context)


def perform_action(request, count: int):
