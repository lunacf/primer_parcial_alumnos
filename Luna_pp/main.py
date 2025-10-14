import sys
import os
import csv
import colorama
colorama.init()

import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
    
from biblioteca.input import get_int
from menu import mostrar_menu
from biblioteca.funciones import (
    cargar_alumnos,
    mostrar_estudiantes,
    buscar_alumno,
    estadisticas,
    ordenar_y_mostrar,
    generar_informe_alumnos
)


def p(message: str) -> None:
  for letter in message:
    print(letter, end='', flush=True)
    time.sleep(0.01)
    
def salir(alumnos):
    print(f"{colorama.Fore.GREEN}¡Hasta luego!{colorama.Style.RESET_ALL}")
    exit()

def init():
    MENU = {
        "1": cargar_alumnos,
        "2": mostrar_estudiantes,
        "3": buscar_alumno,
        "4": estadisticas,
        "5": ordenar_y_mostrar,
        "6": generar_informe_alumnos,
        "7": salir
    }
    
    opciones = [
        f"{colorama.Fore.CYAN}1{colorama.Style.RESET_ALL}. Cargar alumnos",
        f"{colorama.Fore.CYAN}2{colorama.Style.RESET_ALL}. Mostrar alumnos",
        f"{colorama.Fore.CYAN}3{colorama.Style.RESET_ALL}. Buscar alumno",
        f"{colorama.Fore.CYAN}4{colorama.Style.RESET_ALL}. Calcular alumnos",
        f"{colorama.Fore.CYAN}5{colorama.Style.RESET_ALL}. Ordenar y mostrar",
        f"{colorama.Fore.CYAN}6{colorama.Style.RESET_ALL}. Generar informe",
        f"{colorama.Fore.CYAN}7{colorama.Style.RESET_ALL}. Salir"
    ]

    # Creo array de alumnos donde almaceno los datos

    alumnos = []

    while (seleccion := mostrar_menu(f"{colorama.Fore.LIGHTBLACK_EX}Sistema de Gestión de Alumnos", opciones, True)) is not None:
        numero_opcion = str(seleccion + 1)
        if numero_opcion in MENU:
            try:
                MENU[numero_opcion](alumnos)
            except Exception as e:
                print(f"{colorama.Fore.RED}Opción no válida: {e}{colorama.Style.RESET_ALL}")

if __name__ == "__main__":
    init()