from django.shortcuts import render
from django.http import HttpResponse

from .models import Familia
# Create your views here.


def add_familiar(request, nombre, apellido, nacimiento):
    familia=Familia(nombre=nombre,apellido=apellido,nacimiento=nacimiento)
    familia.save()
    return HttpResponse(f"{familia.nombre} agregado!")

def show_familiar(request):
    lista=Familia.objects.all()
    return render(request,"template_familia.html",{"lista_familia":lista})