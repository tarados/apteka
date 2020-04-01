from django.urls import path
from app.views import *


urlpatterns = [
    path('products', products),
    path('pharmacy', pharmacy),
    path('order', order),
    path('order/<int:order_id>', file_order_create),
]