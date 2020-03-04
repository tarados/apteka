from django.urls import path
from app.views import products, pharmacy, order


urlpatterns = [
    path('products', products),
    path('pharmacy', pharmacy),
    path('order', order),
]