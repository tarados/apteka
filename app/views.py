from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt


def index(request):
    books = User.objects.all()
    payload = []
    for book in books:
        payload.append({'id': book.id, 'name': book.username})
    return JsonResponse({'payload': payload})
# Create your views here.
