from django.urls import path

from . import views

app_name = 'curso'
urlpatterns = [
    path('', views.index, name='index'),
    path('alumnos/', views.alumnos, name='alumnos'),
    path('asistencia/', views.asistencia, name='asistencia'),
]