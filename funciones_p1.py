'''
realice un algoritmo que calcule el factorial de un valor ingresado por teclado

 n! = n*(n-1)* (n-2)* ... 1
'''
'''
numero = int(input("Ingrese el valor de n para calcular su factorial: "))
n = numero
factorial = 1
while n > 0:
    factorial *= n #factoril = factorial * n
    n -= 1
print(f"El factorial de factorial de {numero} es: {factorial}")
'''
#funcion que resuelve el factorial del valor que recibe
def algoritmo1(numero):
    n = numero
    factorial = 1
    while n > 0:
        factorial *= n  # factoril = factorial * n
        n -= 1
    return factorial

def sumadosnumeros(a, b):
    return a + b

def areacirculo(radio):
    return radio**2*3.1415


def saludo(nombre="Nombre", apellido="Apellido"):
    print("Hola", nombre, apellido)

'''
print("Antes de llamar a la funcion")
resutlado = algoritmo1(5)
print(f"El resultado es: {resutlado}")

saludo("caselli","nicolas")
saludo(apellido="Caselli", nombre="Nicolás")

Argumentos y parámetros
Pueden ser:
1. Por Posición (primer ejemplo)
2. Por Nombre (segundo ejemplo)
3. Sin Argumentos (def saludo())
4. Por Defecto

saludo()

argumentos indeterminados por posición

'''
def indeterminados_posicion(*args):
    #esta función suma los elementos que se ingresan
    print(f"valor de args: {args}")
    suma =0
    for elemento in args:
        suma += elemento
    return suma


print(indeterminados_posicion(4, 3, 2, 1))

print(indeterminados_posicion(4, 3))
#indeterminados_posicion("hola", "nicolas")
print(indeterminados_posicion())