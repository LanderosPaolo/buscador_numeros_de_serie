# Proyecto: Identificación de Números de Serie en Archivos

Este proyecto consiste en un script de Python que busca y extrae números de serie que siguen un patrón específico en archivos dentro de un directorio dado.

## Detalles del Script

Dependencias:

    re: Módulo para trabajar con expresiones regulares.
    os: Módulo para interactuar con el sistema operativo.
    time: Módulo para medir el tiempo de ejecución.
    datetime: Módulo para trabajar con fechas y horas.
    pathlib: Módulo para manipulación de rutas de archivos y directorios.
    math: Módulo que proporciona funciones matemáticas básicas.

Estructura del Proyecto:

    buscador.py: El script principal que realiza la búsqueda de números de serie.
    Mi_Gran_Directorio/: El directorio que contiene los archivos en los cuales se buscarán los números de serie.

## Resultados

    --------------------------------------------------
    fecha de búsqueda: dd/mm/aaaa
    
    ARCHIVO                 NRO. SERIE
    -------                ----------
    Archivo1.txt           N123-12345
    Archivo2.txt           N456-67890
    
    Números encontrados: 2
    Duración de la búsqueda: x segundos
    --------------------------------------------------
