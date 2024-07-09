from django.urls import path

from .views import flip_coin, flip_cube, get_random_number, perform_action, add_author, add_article, get_articles

urlpatterns = [
    path('flip_coin/<int:count>', flip_coin, name='flip_coin'),
    path('flip_cube/<int:count>', flip_cube, name='flip_cube'),
    path('get_random_number/<int:count>', get_random_number, name='get_random_number'),
    path('perform_action/', perform_action, name='perform_action'),
    path('add_author/', add_author, name='add_author'),
    path('add_article/', add_article, name='add_article'),
    path('get_articles/', get_articles, name='get_articles'),
]