from django.db import models


class Alumno(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Clase(models.Model):
    numero = models.IntegerField(default=0,unique=True)
    def __str__(self):
        return str(self.numero)


class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    asistio = models.IntegerField(default=0)
    class Meta:
        unique_together = (('alumno', 'clase'),)
