from django.test import TestCase
from django.urls import reverse

from .models import Alumno
from .models import Clase
from .models import Asistencia


def create_alumno(nombre):
    return Alumno.objects.create(nombre=nombre)

def create_clase(numero):
    return Clase.objects.create(numero=numero)

def create_asistencia(alumno,clase):
    return Asistencia.objects.create(alumno=alumno,clase=clase)

class GeneralTests(TestCase):
    def test_paginas_vivas(self):
        response = self.client.get(reverse('curso:index'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('curso:alumnos'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('curso:asistencia'))
        self.assertEqual(response.status_code, 200)

class AlumnosTests(TestCase):
    def test_no_alumnos(self):
        response = self.client.get(reverse('curso:alumnos'))
        self.assertQuerysetEqual(
            response.context['lista_alumnos'],
            []
        )

    def test_hay_alumnos(self):
        create_alumno("Alumno de prueba")
        response = self.client.get(reverse('curso:alumnos'))
        self.assertQuerysetEqual(
            response.context['lista_alumnos'],
            ['<Alumno: Alumno de prueba>']
        )

class AsistenciaTests(TestCase):
    def test_asistencia_check(self):
        a = create_alumno("Alumno de prueba")
        c = create_clase(1)
        create_asistencia(a,c)
        response = self.client.get(reverse('curso:asistencia'))
        dict1 = response.context['lista_asistencias']
        dict2 = {str(a.id):[c.id]}
        self.assertQuerysetEqual(
            dict1,
            dict2
        )