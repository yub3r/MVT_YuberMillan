from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar


# Create your views here.

def familiar(self):
    familiar=Familiar(nombre="Carmen", apellido="Martinez", edad="50", directo=1 )
    familiar.save()
    documento= f"Tu familiar {familiar.nombre} {familiar.apellido} es tu {familiar.parentesco}, tiene {familiar.edad} años."
    return HttpResponse(documento)
