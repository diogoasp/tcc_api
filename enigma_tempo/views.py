from urllib import request
from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "index.html", {})

def cartas(request):
    # cartas = {'carta1':{'id':1,'nome':'Claudio', 'custo':3},'carta2':{'id':2,'nome':'Claudilene', 'custo':6}}
    cartas = Card.objects.all()
    return render(request, 'cartas.html', {'cartas':cartas})

def getCarta(request, id):
    #get carta usando id
    cartas = Card.objects.all()
    carta = id
    return render(request, 'cartas.html', {'cartas':cartas, 'carta':carta})

def upload(request):
    cardForm = CardForm()
    result = ''
    if request.method == 'POST':
        upload = CardForm(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            result = '?erro=0'
        else:
            result = '?erro=1'

        
    return render(request,'form.html', {'upload_form': cardForm})