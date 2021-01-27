from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #get text
    djtext = request.POST.get('text', 'default')
    #check checkbox
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    if (removepunc=='on') and (fullcaps=='on') and (charcounter=="on"):
        counter=0
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        t=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        for char in analyzed:
            t=t+char.upper()
        for char in t:
            if char!=" ":
                counter+= 1

        params = {"Purpose": "Remove punctuation and Make upper case",
                  "analyzed_text": t,
                  "counter":counter}
        return render(request, 'analyze.html', params)


    if removepunc=='on':
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={"Purpose":"Remove punctioan",
                "analyzed_text":analyzed}
        return render (request,'analyze.html',params)
    elif (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {"Purpose": "Change to upper case",
                  "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    elif (newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char!='\n':
                analyzed=analyzed+char
        params = {"Purpose": "Remove New Line",
                  "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    elif (extraspaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index] ==' ' and djtext[index+1] ==' '):
                analyzed=analyzed+char
        params = {"Purpose": "Extra space remover",
                  "analyzed_text": analyzed}
        return render(request, 'analyze.html', params)
    elif (charcounter=="on"):
        counter=0
        for char in djtext:
            if char!=" ":
                counter+= 1
        params = {"Purpose": "Character counter",
                  "analyzed_text": counter}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
