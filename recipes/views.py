from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# HTTP REQUEST

def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Ramon'
    })
    # return HTTP RESPONSE


def contato(request):
    return HttpResponse('CONTATO') 


def sobre(request):
    return HttpResponse('SOBRE')