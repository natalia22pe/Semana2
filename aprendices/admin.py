from django.contrib import admin
from .models import Aprendiz, Programa, instructores, Competencias

# Registramos los modelos para que aparezcan en el panel de administración
admin.site.register(Aprendiz)
admin.site.register(Programa)
admin.site.register(instructores)
admin.site.register(Competencias)