from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def removepunc(request):
    #get the text and analyze the text
    djtext=print(request.GET.get('text','default'))
    #print(djtext)
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