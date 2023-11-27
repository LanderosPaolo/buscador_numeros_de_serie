import re
import os
import time
import datetime
from pathlib import Path
import math

# Registra el tiempo de inicio de la ejecución del programa
inicio = time.time()

# Hace la ruta dinámica al directorio del script actual
directorio_actual = Path(__file__).resolve().parent
ruta_relativa = directorio_actual / "Mi_Gran_Directorio"
ruta = str(ruta_relativa)

# Define el patrón a encontrar en los archivos
mi_patron = r"N\D{3}-\d{5}"

# Obtiene la fecha actual
hoy = datetime.date.today()

# Lista que guardará los números de serie encontrados
num_encontrados = []

# Lista que guardará los nombres de archivo encontrados
arc_encontrados = []

def buscar_numero(archivo, patron):
    # Abre el archivo en modo lectura
    abrir = open(archivo, 'r')
    # Lee el contenido del archivo
    texto = abrir.read()
    # Busca el patrón en el texto del archivo
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    # Recorre la estructura de directorios y archivos en la ruta especificada
    for carpeta, subcarpetas, archivo in os.walk(ruta):
        for a in archivo:
            # Busca el patrón en el archivo actual
            resultado = buscar_numero(Path(carpeta, a), mi_patron)
            if resultado != '':
                # Almacena el número de serie encontrado y el nombre de archivo
                num_encontrados.append(resultado.group())
                arc_encontrados.append(a.title())

def mostrar():
    indice = 0
    print("-" * 50)
    print(f"fecha de búsqueda: {hoy.day}/{hoy.month}/{hoy.year}")
    print("\n")
    print("ARCHIVO\t\t\tNRO. SERIE")
    print("-------\t\t\t----------")
    for a in arc_encontrados:
        # Muestra el nombre de archivo y el número de serie correspondiente
        print(f"{a}\t{num_encontrados[indice]}")
        indice += 1
    print("\n")
    print(f"Números encontrados: {len(num_encontrados)}")
    # Calcula y muestra la duración de la búsqueda en segundos
    fin = time.time()
    duracion = fin - inicio
    print(f"Duración de la búsqueda: {math.ceil(duracion)} segundos")
    print("-" * 50)

# Llama a la función para crear las listas de archivos y números de serie
crear_listas()

# Llama a la función para mostrar los resultados
mostrar()