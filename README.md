PARTE 2 – LÓGICA Y ALGORITMIA (Ejercicio Integrador)

Desarrollar en Python un programa modular (usando funciones) que gestione la inscripción de estudiantes a un curso de Programación.
El programa deberá ser operado mediante un menú de opciones en consola y cumplir con las siguientes consignas:

1) Cargar datos de estudiantes

Permitir ingresar los nombres y las notas de N estudiantes (cantidad ingresada por el usuario).

Cada estudiante se representa como un diccionario con las claves "nombre" y "nota".
Los datos deben almacenarse en una lista de estudiantes.
Dicha lista debe guardarse en un archivo alumnos.csv luego de la carga de datos.
Validar que la nota sea un número entero entre 0 y 10.
No se puede acceder a otras opciones hasta que los datos estén cargados.
Si en la carpeta del programa ya existe un archivo alumnos.csv, el sistema deberá cargar automáticamente su contenido (nombres y notas). Al seleccionar la opción 1 del menú, el programa deberá detectar la existencia de dicho archivo y preguntar al usuario: “Se detectó un archivo con información de alumnos. ¿Desea reemplazar los datos existentes o agregar nuevos registros?”

Si elige Reemplazar, se sobrescriben los datos con la nueva carga.
Si elige Agregar, los nuevos estudiantes se añaden a los ya cargados desde el archivo.
El archivo CSV tendrá formato:
nombre,nota
              Ana,9
              Lucas,6

2) Mostrar listado de estudiantes

Mostrar todos los estudiantes con su respectiva nota, en el formato:

Nombre: Ana     | Nota: 9

Nombre: Lucas   | Nota: 6

Separar visualmente con líneas o guiones.

3) Buscar estudiante

Solicitar un nombre y buscarlo en la lista.

Informar si existe o no.
Si existe, mostrar su nota.
La búsqueda no debe distinguir mayúsculas/minúsculas.
4) Calcular estadísticas

Mostrar:

Promedio general del curso.
Cantidad de aprobados (nota ≥ 6) y desaprobados.
Nota más alta y más baja.
5) Ordenar y mostrar

Solicitar al usuario el criterio de ordenamiento (ASC o DESC) y mostrar la lista ordenada por nota según esa elección.

La lista original no debe modificarse (usar una copia).
Validar que el texto ingresado sea correcto, sin importar mayúsculas/minúsculas.
6) Generar informe resumen

Generar un informe final con el siguiente formato:

INFORME FINAL DEL CURSO

-------------------------

Cantidad total de estudiantes: XX

Promedio general: XX.XX

Aprobados: XX

Desaprobados: XX

Mejor nota: X (Alumno: NOMBRE)

Peor nota: X (Alumno: NOMBRE)

-------------------------

Mostrarlo por pantalla y también guardar el texto en un archivo llamado "informe.txt".

7) Salir

Finaliza el programa mostrando un mensaje de despedida.

⚙️ Condiciones

Utilizar funciones para cada punto del menú (por ejemplo: cargar_estudiantes(), buscar_estudiante(), etc.).
Todas las validaciones deben volver a pedir el dato hasta que sea correcto.
No se puede acceder a opciones 2–6 si no se cargaron los datos previamente.
Usar estructuras adecuadas (listas, diccionarios, bucles, condicionales)

<img width="343" height="186" alt="Console" src="https://github.com/user-attachments/assets/fe57911b-89eb-4754-81de-885eca8d1e25" />
