from django.urls import path
from app.views import index, pharmacy, orders


urlpatterns = [
    path('', index),
    path('pharmacy', pharmacy),
    path('orders', orders),
]