from django.urls import path

from .views import get_orders, home, sort_orders_by_period, update_product, upload_img, add_product, display_product

urlpatterns = [
    path('', home, name='home'),
    path('orders/<int:client_id>', get_orders, name='orders'),
    path('orders/<int:client_id>/<int:period>', sort_orders_by_period, name='sort_orders'),
    path('update_product/', update_product, name='update_product'),
    path('upload/', upload_img, name='upload_img'),
    path('add_product/', add_product, name='add_product'),
    path('display_product/', display_product, name='display_product'),
]
