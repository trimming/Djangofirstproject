from django.shortcuts import render
from django.http import HttpResponse
import logging

# Create your views here.
logger = logging.getLogger(__name__)


def home(request):
    logger.info("Index page accessed")
    html = '''
    <!DOCTYPE html>
    <html lang="en">
        
    <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Home</title>            
    </head>
        
    <body>
            <h1>Мой первый сайт Django.</h1>
            <p>Django - это высокоуровневый фреймворк для веб-приложений на языке Python. Он был создан в 2005 году и с 
                тех пор активно развивается и обновляется сообществом разработчиков по всему миру.</p>
            <h2>Обзор фреймворка Django.</h2>
            <p>Django предоставляет разработчикам множество инструментов и функций для создания веб-приложений, таких как:</p>
            <ul>
                <li>ORM (Object-Relational Mapping) для работы с базами данных</li>
                <li>URL-маршрутизация</li>
                <li>Аутентификация и авторизация пользователей</li>
                <li>Шаблонизация</li>
                <li>Кеширование</li>
                <li>Интернационализация</li>
                <li>Административная панель</li>
            </ul>            
    </body>
        
    </html>
    '''
    return HttpResponse(html)


def get_info_about(request):
    logger.info("About page accessed")
    html = '''
    <!DOCTYPE html>
    <html lang="en">
        
    <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>About</title>            
    </head>
        
    <body>
            <h1>Привет, меня зовут Алексей Голиков!</h1>
            <p>Я студент geekbrains факультета веб-разработки. Мне 41 год и у меня нулевой опыт программирования. Но я многому 
            уже научился и продолжаю постигать 'неизведанное')</p>
            <h2>До встречи на семинаре!</h2>                        
    </body>
        
    </html>
    '''
    return HttpResponse(html)