from django.urls import path

from .views import flip_coin, flip_cube, get_random_number

urlpatterns = [
    path('flip_coin/<int:count>', flip_coin, name='flip_coin'),
    path('flip_cube/<int:count>', flip_cube, name='flip_cube'),
    path('get_random_number/<int:count>', get_random_number, name='get_random_number'),
]