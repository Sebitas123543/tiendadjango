from django.shortcuts import render
from .models import EquipoElectronico

def lista_equipos(request):
    equipos = EquipoElectronico.objects.all()
    context = {
        'equipos': equipos,
        'total_equipos': equipos.count()
    }
    return render(request, 'tecnologia/lista_equipos.html', context)