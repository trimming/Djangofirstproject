from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

# Create your views here.
# def home(request):
#     return HttpResponse(f'<h1>Добро пожаловать!</h1>')
#
#
# def random_coin(request):
#     result = random.choice(['орел', 'решка'])
#     return HttpResponse(f'результат: <h1>{result}</h1>')
#
#
# def random_number(request):
#     result = random.randint(0, 100)
#     return HttpResponse(f'Случайное число: {result}')
#
#
# def random_roll(request):
#     result = random.randint(1, 6)
#     return HttpResponse(f'результат броска кубика: {result}')


logger = logging.getLogger(__name__)


def home(request):
    logger.info("Index page accessed")
    return HttpResponse("Hello, world!")


def about(request):
    logger.info("About page accessed")
    return HttpResponse("About Us")


def random_coin(request):
    logger.info("Coin page accessed")
    return HttpResponse(random.choice(["Орёл", "Решка"]))


def random_roll(request):
    logger.info("Cube page accessed")
    result = random.randint(1, 6)
    return HttpResponse(f"Выпал кубик = {result}")


def random_number(request):
    logger.info("Number page accessed")
    result = random.randint(1, 100)
    return HttpResponse(f"Случайное число от 0 до 100 = {result}")
