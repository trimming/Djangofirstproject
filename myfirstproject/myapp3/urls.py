from django.urls import path
from .views import home
from .views import get_info_about

urlpatterns = [
    path('', home, name='home'),
    path('about/', get_info_about, name='about'),
]