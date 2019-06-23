from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
from .models import Alumno,Clase,Asistencia


def index(request):
    return render(request,'curso/index.html')

def alumnos(request):
    nombres = request.POST.get('nombres',False)
    if(nombres):
        for line in nombres.split('\n'):
            a = Alumno(nombre=line)
            a.save()
    lista_alumnos = Alumno.objects.all()
    context = {'lista_alumnos': lista_alumnos}
    return render(request,'curso/alumnos.html', context)

def asistencia(request):
    lista_alumnos = Alumno.objects.all()
    lista_clases = Clase.objects.all()
    lista_asistencias = {}
    if(request.POST.get('actualizo',False)):
        Asistencia.objects.all().delete()
        for a in lista_alumnos:
            clases = request.POST.getlist(str(a.id),False)
            if(clases):
                lista_asistencias[a.id] = []
                for c in clases:
                    asist = Asistencia(alumno=a,clase=Clase.objects.get(id=int(c)),asistio=1)
                    asist.save()
                    lista_asistencias[a.id].append(int(c))
    else:
        for asist in Asistencia.objects.all():
            if asist.alumno.id not in lista_asistencias:
                lista_asistencias[asist.alumno.id] = []
            lista_asistencias[asist.alumno.id].append(asist.clase.id)

    context = {'lista_alumnos': lista_alumnos, 'lista_clases': lista_clases, 'lista_asistencias': lista_asistencias}
    return render(request,'curso/asistencia.html', context)