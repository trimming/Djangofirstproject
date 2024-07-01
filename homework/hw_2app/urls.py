from django.urls import path

from .views import get_orders, home

urlpatterns = [
    path('', home, name='home'),
    path('orders/<int:client_id>', get_orders, name='orders'),
]