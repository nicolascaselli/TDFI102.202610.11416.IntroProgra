'''

Realice un programa que cree un archivo llamado mensaje.txt y escriba dentro de él el mensaje:
Hola, este es mi primer archivo en Python.
'''

#Escribir información en un archivo
'''
varLista = ['estudiante 1', 5.5, 'Estudiante 2', 6.6]
with open("mensaje.txt", "w") as elcontenido:
    elcontenido.write("Hola, este es mi primer archivo en Python.\n")
    elcontenido.write(str(varLista))

#como leemos información de un archivo
with open("mensaje.txt", "r") as elArchivo:
    contenido = elArchivo.read()

print("El contenido del archivo es: ")
print(contenido)
'''

'''
Realice un programa que solicite al usuario tres nombres y los guarde en un archivo llamado nombres.txt, uno por línea.

#ingresar nombres en un archivo
with open("nombres.txt", "w", encoding="utf-8") as archivo:
    for nombre in range(3):
        nombre = input("Ingrese el nombre: ")
        archivo.write(nombre+"\n")

print("Todos los nombres han sido registrados en el archivo")
'''
'''
Utilizando el archivo nombres.txt, realice un programa que lea los nombres guardados, los muestre por pantalla y cuente cuántos nombres contiene el archivo.
'''
'''
contador = 0
with open("nombres.txt", "r", encoding="utf-8") as archivo:
    for linea_archivo in archivo:
        nombre = linea_archivo.strip() #con strip le quitamos el salto de línea final
        print("El nombre es: ", nombre)
        contador += 1 #contador = contador +1
print(f"La cantidad de nombres es: {contador}")
'''
'''
Realice un programa que solicite al usuario el nombre de tres estudiantes y su respectiva nota final. Los datos deben guardarse en un archivo llamado notas.txt, usando el siguiente formato:
nombre;nota

Por ejemplo:
Ana;6.5
Luis;5.8
Camila;4.7

with open("notas.txt", "w", encoding="utf-8") as archivo:
    for i in range(3):
        nombre = input("Ingrese el nombre del estudiante: ")
        nota = float(input("Ingrese la nota final: "))
        archivo.write(nombre + ";" + str(nota) + "\n")

print("Notas guardadas correctamente.")
'''
'''
Utilizando el archivo notas.txt, realice un programa que lea todas las notas registradas y calcule el promedio del curso.
'''
sumatoria = 0
conteo = 0
with open("notas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        datos = linea.strip().split(";") #quita el salto de línea y separa los datos usando el punto y coma como separador, y los retorna como lista
        nombre = datos[0]
        nota = float(datos[1])

        sumatoria += nota
        conteo += 1

if conteo >0:
    promedio = sumatoria/conteo
    print(f"El promedio del curso es: {promedio}")
else:
    print("No habían notas registradas")


'''
Utilizando el archivo notas.txt, realice un programa que muestre el nombre, la nota y la condición de cada estudiante. Se considera aprobado si la nota es mayor o igual a 4.0.
'''

