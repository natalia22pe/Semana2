from django.shortcuts import render
from.models import Aprendiz 

# Create your views here.
def  index (request):
    #consultamos todos los aprendices registrados 
     aprendices = Aprendiz.objects.all()

     #pasamos el queryset dentro del diccionario del contexto
     
     contexto ={
          'aprendices': aprendices
     }

     return render (request, 'aprendices/index.html', contexto )