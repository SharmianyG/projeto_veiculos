from django.contrib import admin

# Register your models here.
from app_veiculos.models import TiposDeVeiculos, MarcaDoVeiculo, Veiculos

admin.site.register(TiposDeVeiculos)
admin.site.register(MarcaDoVeiculo)
admin.site.register(Veiculos)
