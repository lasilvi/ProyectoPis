from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from .models import *
from openpyxl import load_workbook

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('importar_datos')
            else:
                return render(request=request, template_name="registro/login.html", context={'form': form})
        else:
            for key, error in list(form.errors.items()):
                messages.error(request, error)
    form = UserLoginForm()
    return render(request=request, template_name="registro/login.html", context={'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def importar_datos(request):
    if request.method == 'POST':
        form = ImportarDatosForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_excel = form.cleaned_data['archivo_excel']
            procesar_archivo_excel(archivo_excel)
            print("datos importados")
            return redirect('importar_datos') 
        else:
            print("no valido")# Redirige a la página de importación de datos
    else:
        form = ImportarDatosForm()
    return render(request, 'appseguimiento/index.html', {'form': form})

def procesar_archivo_excel(archivo_excel):
    wb = load_workbook(archivo_excel)
    print("aqui llege")
    hoja = wb.active

    for fila in hoja.iter_rows(min_row=2, values_only=True):
        # Supongamos que la primera columna contiene nombres y la segunda columnas contiene valores
        equipo = Equipos(
            servicio=fila[0], 
            equipo=fila[1],
            ubicacion=fila[2],
            sede=fila[3],
            etiqueta_caja=fila[4],
            factura_contrato=fila[5],
            resolucion_invima=fila[6],
            carta_garantia=fila[7],
            acta_entrega=fila[8],
            declaracion_importacion=fila[9],
            cronograma_mantenimiento=fila[10],
            cronograma_calibracion=fila[11],
            reportes_mantenimiento=fila[12],
            reportes_calibracion=fila[13],
            guia_rapida=fila[14],
            manual_usuario_espanol=fila[15],
            manual_servicio_espanol=fila[16],
            hoja_vida_calibracion=fila[17],
            hoja_vida_mantenimiento=fila[18],
            contrato_mantenimiento=fila[19],
            contrato_calibracion=fila[20]
        )
        equipo.save()