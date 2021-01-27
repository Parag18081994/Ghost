# I hace created this file-PN

from django.http import HttpResponse
def index(request):
    return HttpResponse('''<H1>Navigation for Parag</H1><a href='https://www.youtube.com/watch?v=zs2Ux1jfDD0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=6'>Here is the playlist</a><br>
                        <a href="https://developers.google.com/edu/python/regular-expressions">Google</a><br>
                        <a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-6">flipkart</a>''')

def about(request):
    return HttpResponse("About!! Parag")