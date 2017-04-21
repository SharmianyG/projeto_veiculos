from django.shortcuts import render

# Create your views here.
from app_veiculos.models import Veiculos


def index(request):

    consulta_no_banco = Veiculos.objects.all()

    return render(request,'index.html', {'consulta_no_banco':consulta_no_banco})


