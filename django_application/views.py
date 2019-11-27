from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hello World from Django")

def despedida(request):
    
    HTML = """<body>
        <div>
            <h1>GoodBye From Django</h1>
        </div>
    </body>"""

    return HttpResponse(HTML)

def getDate(request):
    now = datetime.datetime.now()
    return HttpResponse(now)

def calculateAge(request, year):
    #return HttpResponse(year)
    edadActual = 24
    periodo = year-2019
    edadFutura = edadActual+periodo
    html = "<h2>En el año %s tendrás %s años</h2>" %(year,edadFutura)
    return HttpResponse(html)
