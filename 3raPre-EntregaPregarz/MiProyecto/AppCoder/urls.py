from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("compus/", computadora, name = "Compus"),
    path("perif/", perifericos, name = "Perif"),
    
    path("platfo/", plataforma, name = "Platfo"),
    
    #urls de creacion
    path("formuCompu/", compuFormulario, name = "CompuFormulario"),
    path("formuPerif/", periFormulario, name = "PeriFormulario"),
    
    path("formuPlata/", plataFormulario, name = "PlataFormulario"),
    
    #urls de busqueda
    path("busquedaPlacaVideo/", busquedaPlacaVideo, name = "BusquedaPlacaVideo"),
    path("busquedaTeclado/", busquedaTeclado, name = "BusquedaTeclado"),
    
    path("busquedaPlata/", busquedaPlata, name = "BusquedaPlata"),
    
    #urls de resultado
    path("resultadoPlacaVideo/", resultadoPlacaVideo, name = "ResultadoPlacaVideo"),
    path("resultadoTeclado/", resultadoTeclado, name = "ResultadoTeclado"),
    
    path("resultadoPlata/", resultadoPlata, name = "ResultadoPlata"),
]
