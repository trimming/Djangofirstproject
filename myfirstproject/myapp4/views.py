import logging

from django.shortcuts import render, redirect
from .models import Author, Article
# Create your views here.
from .forms import RandomGame, AuthorForm, ArticleForm
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


def perform_action(request):
    if request.method == 'POST':
        form = RandomGame(request.POST)
        if form.is_valid():
            event_type = form.cleaned_data['event_type']
            attempts = form.cleaned_data['attempts']
            if event_type == 'coin':
                return flip_coin(request, attempts)
            elif event_type == 'dice':
                return flip_cube(request, attempts)
            else:
                return get_random_number(request, attempts)
    else:
        form = RandomGame()
    return render(request, 'myapp4/games_form.html', {'form': form})


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            author = Author.objects.create(name=form_data['name'], last_name=form_data['last_name'],
                                           email=form_data['email'], bio=form_data['bio'],
                                           birthday=form_data['birthday'])
    else:
        form = AuthorForm()
    authors = Author.objects.all()
    context = {
        'authors': authors,
        'form': form,
    }
    return render(request, 'myapp4/authors.html', context)


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            Article.objects.create(title=form_data['title'],
                                             text=form_data['text'],
                                             author=form_data['author'],
                                             category=form_data['category'],
                                             is_published=form_data['is_published'])
            return redirect('get_articles')
    else:
        form = ArticleForm()
    return render(request, 'myapp4/games_form.html', {'form': form})


def get_articles(request, author_id: int=None):
    if author_id:
        author = Author.objects.filter(id=author_id).first()
        articles = Article.objects.filter(author=author)
        title = f'Статьи автора: {author.full_name()}'
    else:
        title = 'Все статьи'
        articles = Article.objects.all()
    context = {
        'title': title,
        'articles_list': articles,
    }
    return render(request, 'myapp4/get_articles.html', context)