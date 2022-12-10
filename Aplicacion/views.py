from django.shortcuts import render
from django.http import HttpResponse
from .models import Familiar

# Create your views here.

def familiar(request):
    familiar1 = Familiar(nombre="Ayelen", edad=23, anio_nacimiento="1999-6-6")
    familiar1.save()
    familiar2 = Familiar(nombre="Bruno", edad=20, anio_nacimiento="2002-11-28")
    familiar2.save()
    familiar3 = Familiar(nombre="Castulo", edad=72, anio_nacimiento="1950-4-27")
    familiar3.save()
    return render(
        request,
        "padre.html",
        {"familiares": [familiar1, familiar2, familiar3]},
    )
