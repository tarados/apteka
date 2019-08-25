from django.urls import path
from app.views import index, farmacy


urlpatterns = [
    path('', index),
    path('farmacy', farmacy),
]