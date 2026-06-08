'''

def dividir(a, b=1):
    if b == 0:
        return 1
    return a / b

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

print(f"la división de a ={valor1} y b = {valor2} es: {dividir(valor1, valor2)}")


Genera una función que reciba como parámetro el nombre el Ruth el apellido la edad el género signo zodiacal fecha de cumpleaños comida preferida estilo musical de un estudiante y esos valores se guarden en un archivo separado por,
el archivo se debe llamar BDClientes.txt, si el archivo no existe, se crea uno nuevo
la función se debe llamar guardacliente, y recibe todos los parámetros antes indicados
'''
def guardacliente(nombre, apellido, rut, edad, zodiaco="Virgo", nacimiento="19000101", comidafav="", estilomusical=""):
    with open("BDClientes.txt", "a") as file:
        file.write(nombre +"," +
        apellido +"," +
        rut +"," +
        str(edad) +"," +
        zodiaco +"," +
           nacimiento+"," +
           comidafav + "," +
           estilomusical + "\n")


guardacliente(rut="9999999-9", edad=39, comidafav="pollo", estilomusical="funk", nacimiento="20200101",nombre="Andrés", apellido="Silva")


def guardaClientesIndeterminados(*clientes):
    with open("BDClientes.txt", "a") as file:
        for cliente in clientes:
            file.write(cliente +",")
        file.write("\n")


guardaClientesIndeterminados("Nicolas", "Caselli", "41", "Virgo", "Pizza", "Cumbia")


