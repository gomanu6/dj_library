from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    htpr = {
        'scheme': request.scheme,
        'body': request.body,
        'path': request.path,
        'path_info': request.path_info
    }
    output = f'The HttpResponse header is {request.headers["User-Agent"]}'
    return HttpResponse(output)
