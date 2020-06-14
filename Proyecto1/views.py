from django.http import HttpResponse

#Creamos una vista 
def saludo(request):

    return HttpResponse("Esta es mi primera pagina con Django")