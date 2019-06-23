from django.contrib import admin

# Register your models here.

from .models import Alumno
from .models import Clase
from .models import Asistencia

admin.site.register(Alumno)
admin.site.register(Clase)
admin.site.register(Asistencia)

