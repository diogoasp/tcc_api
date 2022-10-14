from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html", {})

def cartas(request):
    cartas = ['carta1', 'carta2', 'carta3', 'carta4']
    return render(request, 'cartas.html', {'cartas':cartas})