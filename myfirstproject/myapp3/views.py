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