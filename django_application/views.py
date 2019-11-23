from django.http import *

def saludo(request):
    return HttpResponse("Hello World from Django")

def despedida(request):
    return HttpResponse("<h1>Goodbye from Django</h1>")