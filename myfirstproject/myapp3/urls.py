from django.urls import path
from .views import home, get_info_about, flip_cube, flip_coin, get_random_number, get_articles, get_post

urlpatterns = [
    path('', home, name='home'),
    path('about/', get_info_about, name='about'),
    path('game_coin/<int:count>', flip_coin, name='game_coin'),
    path('game_cube/<int:count>', flip_cube, name='game_cube'),
    path('game_number/<int:count>', get_random_number, name='game_number'),
    path('news/<int:author_id>', get_articles, name='news'),
    path('post/<int:post_id>', get_post, name='post'),
]