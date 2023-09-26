from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
from AppCoder.forms import *
# Create your views here.
# Vistas default


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def computadora(request):
    return render(request, "AppCoder/computadoras.html")
    
def perifericos(request):
    return render(request, "AppCoder/perifericos.html")
    

    
def plataforma(request):
    return render(request, "AppCoder/plataforma.html")


#Vistas Formularios POST


def compuFormulario(request):
    if request.method == "POST":  #funciona si damos click a enviar
        formulario1 = CompuFormulario(request.POST)
        
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            
            compu = Computadora(
                placaMadre = info["placa_madre"],
                placaVideo = info["placa_de_video"],
                procesador = info["procesador"],
                ram = info["ram"],
                fuente = info["fuente"],
                almacenamiento = info["almacenamiento"],
                )
            
            compu.save()
            
            return render(request, "AppCoder/computadoras.html")
        
    else:
        formulario1 = CompuFormulario()
            
                
    return render(request, "AppCoder/formuCompu.html", {"form1" : formulario1})


def periFormulario(request):
    if request.method == "POST":
        formulario2 = PeriFormulario(request.POST)
    
        if formulario2.is_valid():
            info = formulario2.cleaned_data
        
            peri = Perifericos(
                teclado = info["teclado"],
                mouse = info["mouse"],
                monitor = info["monitor"],
                headset = info["headset"],
                )
        
            peri.save()
        
            return render(request, "AppCoder/perifericos.html")
    
    else:
        formulario2 = PeriFormulario()
        
    return render(request, "AppCoder/formuPerif.html", {"form2" : formulario2})





def plataFormulario(request):
    if request.method == "POST":
        formulario4 = PlataFormulario(request.POST)
        
        if formulario4.is_valid():
            info = formulario4.cleaned_data
            
            plata = Plataforma(
                nombrePlataforma = info["nombre_plataforma"],
                user = info["user"],
                mail = info["mail"],
            )
            
            plata.save()
            
            return render(request, "AppCoder/plataforma.html")
        
    else:
        formulario4 = PlataFormulario()
        
    return render(request, "AppCoder/formuPlata.html", {"form4" : formulario4})


# vista formulario GET

def busquedaPlacaVideo(request):
    return render(request, "AppCoder/busquedaPlacaVideo.html")

def busquedaTeclado(request):
    return render(request, "AppCoder/busquedaTeclado.html")



def busquedaPlata(request):
    return render(request, "AppCoder/busquedaPlata.html")



#vista resultados busqueda

def resultadoTeclado(request):
    if request.GET["teclado"]:
        keyboard = request.GET["teclado"]
        resuTeclado = Perifericos.objects.filter(teclado__icontains=keyboard)
        
        return render(request, "AppCoder/resultadoTeclado.html", {"keyboard" : keyboard, "resu" : resuTeclado})
    
    else:
        return render(request, "AppCoder/busquedaTeclado.html")

def resultadoPlacaVideo(request):
    if request.GET["placaVideo"]:
        placaVid = request.GET["placaVideo"]
        resuPlacaVid = Computadora.objects.filter(placaVideo__icontains=placaVid) 
        
        return render(request, "AppCoder/resultadosPlacaVideo.html", {"placaVid" : placaVid, "res" : resuPlacaVid})
    
    else:
        return render(request, "AppCoder/busquedaPlacaVideo.html")
    

        

def resultadoPlata(request):
    if request.GET["plataforma"]:
        plataforma = request.GET["plataforma"]
        resuPlata = Plataforma.objects.filter(nombrePlataforma__icontains=plataforma)
        
        return render(request, "AppCoder/resultadoPlata.html", {"plataforma" : plataforma, "result" : resuPlata})
    
    else:
        return render(request,"AppCoder/busquedaPlata.html")
    
    
    
    
    

        