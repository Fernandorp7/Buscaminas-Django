from django.shortcuts import render
from .forms import CreaTableroForm
from .tablero import tablero

def welcome(request):
    return render(request, "buscaminas2/index.html")

def crea_tablero(request):
    if request.method == 'POST':
        tablero_form = CreaTableroForm(request.POST)

        if tablero_form.is_valid():
            columnas = int(tablero_form.cleaned_data['columnas'])
            filas = int(tablero_form.cleaned_data['filas'])
            minas = int(tablero_form.cleaned_data['minas'])
            lista_filas = range(filas)
            lista_columnas = range(columnas)

            mi_tablero = tablero(columnas, filas, minas)

            return render(request, 'buscaminas2/muestra_tablero.html',
                          {'form': tablero_form, "tablero": mi_tablero})

    else:
        tablero_form = CreaTableroForm()

    return render(request, 'buscaminas2/crea_tablero.html', {'tablero_form': tablero_form})
