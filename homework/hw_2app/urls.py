from django.urls import path

from .views import get_orders, home, sort_orders_by_period, update_product, upload_img

urlpatterns = [
    path('', home, name='home'),
    path('orders/<int:client_id>', get_orders, name='orders'),
    path('orders/<int:client_id>/<int:period>', sort_orders_by_period, name='sort_orders'),
    path('update_product/', update_product, name='update_product'),
    path('upload/', upload_img, name='upload_img'),
]