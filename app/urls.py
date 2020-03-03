from django.urls import path
from app.views import index, pharmacy, order


urlpatterns = [
    path('', index),
    path('pharmacy', pharmacy),
    path('order', order),
]