from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params={'name':'parag',
            'place':'Jupiter'}
    return render (request,'index.html',params)
    #return  HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse('''<H1>Capitalize first<H1><br> 
   <button onclick="location.href='http://127.0.0.1:8000/removepunc'">Click me</button>''')

def newlineremove(request):
    return HttpResponse('new line remove')

def spaceremover(request):
    return HttpResponse('space remover')

def charcount(request):
    return HttpResponse('character counter')