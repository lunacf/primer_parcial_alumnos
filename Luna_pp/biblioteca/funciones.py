import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
import csv
import colorama
colorama.init()
from datetime import datetime

from biblioteca.input import get_int, get_string, get_float
from menu import mostrar_menu


def cargar_alumnos(alumnos: list[dict]) -> None:
    print(f"{colorama.Fore.GREEN}Cargar estudiantes UTN: {colorama.Style.RESET_ALL}")
    
    opcion = 1
    
    if os.path.exists("alumnos.csv"):
        opcion = get_int("Se detectó un archivo con información de alumnos. ¿Desea reemplazar los datos existentes (1) o agregar nuevos registros (2)? ", "Opción no válida", 1, 2, 3)
        if opcion == None: 
            print("Opción no válida.")
            return
    
    if opcion == 1:
        # Aca limpio la lista y creo nuevo archivo alumnos.csv
        alumnos.clear()
        with open("alumnos.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "nota"])
            
    elif opcion == 2:
        with open("alumnos.csv", "r") as file:
            reader = csv.DictReader(file)
            alumnos.clear()  
            for row in reader:
                alumnos.append({
                    'nombre': row['nombre'],
                    'nota': float(row['nota'])
                })
    else: 
        # Aca creo nuevo archivo en caso de que no existiera...
        with open("alumnos.csv", "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["nombre", "nota"])
    
    while True:
        print(f"{colorama.Fore.BLUE}Ingrese los datos del estudiante:{colorama.Style.RESET_ALL}")
        nombre = get_string("Nombre: ", "Nombre no válido", 1, 50, 3)
        if nombre is None:
            print("No se pudo obtener un nombre válido. Saliendo de la carga de estudiantes.")
            break

        print(f"{colorama.Fore.LIGHTBLACK_EX}Ingrese la nota del estudiante (0-10): {colorama.Style.RESET_ALL}")
        nota = get_float("Nota: ", "Nota no válida", 0, 10, 3)
        if nota is None:
            print("No se pudo obtener una nota válida. Saliendo de la carga de estudiantes.")
            break

        alumnos.append({
            'nombre': nombre,
            'nota': nota
        })
        
        print(f"{colorama.Fore.GREEN}✅ Alumno {nombre} agregado correctamente.{colorama.Style.RESET_ALL}")
        
        
        # Si quisiera cargar otro alumno más, lo pregunto
        continuar = get_int("¿Desea cargar otro estudiante? (1: Sí, 2: No): ", "Opción no válida", 1, 2, 3)
        if continuar is None or continuar == 2:
            print("Finalizando carga de estudiantes...")
            break

    with open("alumnos.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["nombre", "nota"])
        for alumno in alumnos:
            writer.writerow(alumno)


def mostrar_estudiantes(lista_alumnos: list[dict]) -> None:
    if len(lista_alumnos) == 0:
        print("No hay alumnos cargados.\n")
        return

    print(f"{colorama.Fore.GREEN}{colorama.Style.BRIGHT} CENTRO DE ALUMNOS CARGADOS EN EL SISTEMA{colorama.Style.RESET_ALL}")
    print(colorama.Fore.YELLOW + "=" * 110 + colorama.Style.RESET_ALL)

    for alumno in lista_alumnos:
        
        # si la nota es menor a 6 es desaprobado y se pinta de rojo
        if alumno['nota'] < 6:
            color_estado = colorama.Fore.RED + colorama.Style.BRIGHT
        elif alumno['nota'] >= 8:
            color_estado = colorama.Fore.GREEN + colorama.Style.BRIGHT
        else:
            color_estado = colorama.Fore.YELLOW 
        
        print(f"{color_estado}Nombre: {alumno['nombre']} | Nota: {alumno['nota']}{colorama.Style.RESET_ALL}")

def buscar_alumno(lista_alumnos: list[dict]) -> None:
    if len(lista_alumnos) == 0:
        print("No hay alumnos cargados.\n")
        return
    
    nombre_buscar = get_string(f"{colorama.Fore.CYAN}Ingrese el nombre del alumno a buscar:{colorama.Style.RESET_ALL}", "Nombre no válido", 1, 50, 3)
    if nombre_buscar is None:
        print("No se pudo obtener un nombre válido.")
        return
    encontrados = [alumno for alumno in lista_alumnos if alumno['nombre'].lower() == nombre_buscar.lower()]
    
    if encontrados:
        print(f"{colorama.Fore.GREEN}Alumnos encontrados:{colorama.Style.RESET_ALL}")
        for alumno in encontrados:
            print(f"Nombre: {alumno['nombre']} | Nota: {alumno['nota']}")
            

def estadisticas(lista_alumnos: list[dict]) -> None:
    if len(lista_alumnos) == 0:
        print("No hay alumnos cargados.\n")
        return
    
    total_alumnos = len(lista_alumnos)
    suma_notas_total = sum(alumno['nota'] for alumno in lista_alumnos)
    promedio_general = suma_notas_total / total_alumnos
    aprobados = sum(1 for alumno in lista_alumnos if alumno['nota'] >= 6)
    desaprobados = total_alumnos - aprobados
    nota_mas_alta = max(alumno['nota'] for alumno in lista_alumnos)
    nota_mas_baja = min(alumno['nota'] for alumno in lista_alumnos)

    print(f"{colorama.Fore.CYAN}Estadísticas del curso:{colorama.Style.RESET_ALL}")
    print(f"Promedio general: {promedio_general:.2f}")
    print(f"Cantidad de aprobados: {aprobados}")
    print(f"Cantidad de desaprobados: {desaprobados}")
    print(f"Nota más alta: {nota_mas_alta}")
    print(f"Nota más baja: {nota_mas_baja}")
    
# Ordenar y mostrar alumnos

def ordenar_y_mostrar(lista_alumnos: list[dict]) -> None:
    if len(lista_alumnos) == 0:
        print(f"{colorama.Fore.RED}No hay alumnos cargados.{colorama.Style.RESET_ALL}\n")
        return
    
    opciones_orden = [
        f"Ordenar por nombre ascendente",
        f"Ordenar por nombre descendente",
    ]

    orden_index = mostrar_menu("Seleccione el criterio de ordenamiento", opciones_orden)
    if orden_index is None:
        print("Operación cancelada.")
        return
    
    reverso = orden_index == 1
    # Aca ordeno la lista de alumnos por nombre usando lambda
    alumnos_ordenados = sorted(lista_alumnos, key=lambda x: x['nombre'].lower(), reverse=reverso)

    titulo = "Alumnos ordenados por valor (Mayor o Menor) " if reverso else "Alumnos ordenados por valor (Menor a Mayor) "
    print(f"{colorama.Fore.CYAN}{titulo}{colorama.Style.RESET_ALL}")

    # Clave valor para ordenar por nota
    for alumno in alumnos_ordenados:
        print(f"{titulo} Nombre: {alumno['nombre']} | Nota: {alumno['nota']}")

    
def generar_informe_alumnos(lista_alumnos: list[dict]) -> None:
    if len(lista_alumnos) == 0:
        print("No hay alumnos cargados.\n")
        return
    
    try:
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        total_alumnos = len(lista_alumnos)
        suma_notas = sum(alumno['nota'] for alumno in lista_alumnos)
        promedio_general = suma_notas / total_alumnos
        aprobados = sum(1 for alumno in lista_alumnos if alumno['nota'] >= 6)
        desaprobados = total_alumnos - aprobados
        nota_mas_alta = max(alumno['nota'] for alumno in lista_alumnos)
        nota_mas_baja = min(alumno['nota'] for alumno in lista_alumnos)
        
        # Encontrar alumno con mejor y peor nota
        alumno_mejor = next(alumno for alumno in lista_alumnos if alumno['nota'] == nota_mas_alta)
        alumno_peor = next(alumno for alumno in lista_alumnos if alumno['nota'] == nota_mas_baja)
        
        with open("informe.txt", "w", encoding="utf-8") as file:
            # Aca genero el contenido de informe.txt
            file.write("INFORME FINAL DEL CURSO\n")
            file.write("-------------------------\n")
            file.write(f"Cantidad total de estudiantes: {total_alumnos}\n")
            file.write(f"Promedio general: {promedio_general:.2f}\n")
            file.write(f"Aprobados: {aprobados}\n")
            file.write(f"Desaprobados: {desaprobados}\n")
            file.write(f"Mejor nota: {nota_mas_alta} (Alumno: {alumno_mejor['nombre']})\n")
            file.write(f"Peor nota: {nota_mas_baja} (Alumno: {alumno_peor['nombre']})\n")
            file.write("-------------------------\n")
            file.write(f"Fecha de generación: {fecha_actual}\n")
        
        # Muestro el informe por pantalla en el tiempo de ejecución
        print(f"\n{colorama.Fore.CYAN}INFORME FINAL DEL CURSO{colorama.Style.RESET_ALL}")
        print("-------------------------")
        print(f"Cantidad total de estudiantes: {total_alumnos}")
        print(f"Promedio general: {promedio_general:.2f}")
        print(f"Aprobados: {aprobados}")
        print(f"Desaprobados: {desaprobados}")
        print(f"Mejor nota: {nota_mas_alta} (Alumno: {alumno_mejor['nombre']})")
        print(f"Peor nota: {nota_mas_baja} (Alumno: {alumno_peor['nombre']})")
        print("-------------------------")
        
        print(f"\n{colorama.Fore.GREEN}✅ Informe generado exitosamente en 'informe.txt'{colorama.Style.RESET_ALL}")

    except Exception as e:
        print(colorama.Fore.RED + f"❌ Error al generar el informe: {e}" + colorama.Style.RESET_ALL)
