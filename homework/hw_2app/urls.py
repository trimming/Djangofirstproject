from django.urls import path

from .views import get_orders, home, sort_orders_by_period

urlpatterns = [
    path('', home, name='home'),
    path('orders/<int:client_id>', get_orders, name='orders'),
    path('orders/<int:client_id>/<int:period>', sort_orders_by_period, name='sort_orders'),
]