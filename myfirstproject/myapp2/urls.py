from django.urls import path
from .views import coin_flip

urlpatterns = [
    path('', coin_flip, name='coin_flip'),
]