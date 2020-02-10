from django.urls import path
from app.views import index, farmacy, orders


urlpatterns = [
    path('', index),
    path('farmacy', farmacy),
    path('orders', orders),
]