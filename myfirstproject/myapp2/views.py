from django.shortcuts import render
from .models import CoinFlip
from django.shortcuts import render


# Create your views here.


def coin_flip(request):
    flip = CoinFlip.get_last_flip(3)
    return render(request, 'index.html', {'flip': flip})
