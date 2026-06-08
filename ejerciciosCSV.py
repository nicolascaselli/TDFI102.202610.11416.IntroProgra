import csv

def cargar_estudiantes(nombre_archivo):
    estudiantes = []

    with open(nombre_archivo, "r", encoding="utf-8-sig") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            estudiantes.append(fila)

    return estudiantes


estudiantes = cargar_estudiantes("base_notas_introduccion_programacion_300_estudiantes.csv")
print("Cantidad de estudiantes cargados:", len(estudiantes))
#print(estudiantes)
print(f"El estudiante en la posición 300:{estudiantes[299]}")

'''
ejercicio 1:
Crear una función llamada mostrar_estudiante que reciba un diccionario correspondiente a un estudiante y muestre sus principales datos personales y académicos.
'''

def mostrar_estudiante(estudiante):
    print(f"ID: {estudiante['id_estudiante']}")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Apellido paterno: {estudiante['apellido_paterno']}")
    print(f"Apellido materno: {estudiante['apellido_materno']}")
    print(f"Sección: {estudiante['seccion']}")
    print(f"Jornada: {estudiante['jornada']}")
    print(f"Nota Final: {estudiante['nota_final']}")
    print(f"Estado: {estudiante['estado']}")


#mostrar_estudiante(estudiantes[299])

'''
Crear una función llamada obtener_nombre_completo que reciba un diccionario de estudiante y retorne su nombre completo.
'''

def mostrar_claves(estudiante):
    for clave in estudiante.keys():
        print(f"Clave: {clave}")
print(estudiantes[299].keys())
print(estudiantes[299].items())
mostrar_claves(estudiantes[299])


def mostrar_diccionario_completo(estudiante):
    for clave, valor in estudiante.items():
        print(clave, ":", valor)

mostrar_diccionario_completo(estudiantes[299])

'''
crea una función llamada estadisticas_estudiante, que reciba un estudiante, y retorne 3 valores, la nota mínima, máxima y su promedio
return val1, val2, val3

a, b, c = func(queretorna3valores)

'''