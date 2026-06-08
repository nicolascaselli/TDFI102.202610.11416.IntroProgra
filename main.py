varLista = [3, 8, 12, 10]
print(varLista)
print(type(varLista))
#mostrar el elemento en la posición 2
print(varLista[1])
print(type(varLista[1]))
#obtener la cantidad de elementos de una lista
print(len(varLista))

for elemento in varLista:
    print(f"Elemento: {elemento}")

print("Fin del for")

for elemento in range(10):
    print(f"Elemento: {elemento}")

print("Fin del for")

#Genera un programa en Python, que permita al usuario ingresar cinco calificaciones de un estudiante utilizando listas
listaNotas = []
for nota in range(5):
    listaNotas.append(float(input("Ingrese nota: ")))
    #listaNotas[nota] = float(input(f"Ingresa nota: ")) //se usa solo para asignación cuándo ya tiene espacios asignados

#mostrar las notas ingresadas con un hermoso for
cantidad = 1
for nota in listaNotas:
    print(f"Nota {cantidad}: {nota}")
    cantidad += 1 #cantidad = cantidad +1


