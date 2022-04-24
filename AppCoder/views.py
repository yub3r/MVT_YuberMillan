from pydoc import plain
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from AppCoder.models import Familiar


# Create your views here.

def familiar(self):
    familiar1=Familiar(nombre="Carmen", apellido="Martinez", parentesco="madre", edad="50", directo=1 )
    familiar1.save()
    familiar2 = Familiar(nombre="Alberto", apellido="Millan", parentesco="padre", edad="55", directo=1)
    familiar2.save()
    familiar3 = Familiar(nombre="Yoel", apellido="Millan", parentesco="hermano", edad="22", directo=1)
    familiar3.save()




    diccionario={
        "f1nombre":familiar1.nombre,
        "f1apellido":familiar1.apellido,
        "f1parentesco":familiar1.parentesco,
        "f1edad":familiar1.edad,
        "f2nombre":familiar2.nombre,
        "f2apellido":familiar2.apellido,
        "f2parentesco":familiar2.parentesco,
        "f2edad":familiar2.edad,
        "f3nombre":familiar3.nombre,
        "f3apellido":familiar3.apellido,
        "f3parentesco":familiar3.parentesco,
        "f3edad":familiar3.edad,
    }
    
    plantilla= loader.get_template('familyweb.html')
    documento= plantilla.render(diccionario)
    return HttpResponse(documento)




    # documento= f"Tu familiar, {familiar1.nombre} {familiar1.apellido} es tu {familiar1.parentesco} y tiene {familiar1.edad} años." 
    # documento= f"Tu familiar, {familiar2.nombre} {familiar2.apellido} es tu {familiar2.parentesco} y tiene {familiar2.edad} años." 
    # documento= f"Tu familiar, {familiar3.nombre} {familiar3.apellido} es tu {familiar3.parentesco} y tiene {familiar3.edad} años." 
    # return HttpResponse(documento)