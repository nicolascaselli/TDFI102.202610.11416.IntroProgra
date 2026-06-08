class Paciente:
    def __init__(self, rut_paciente, primer_nombre, apellido_paterno, edad, presupuesto, prevision="Fonasa"):
        self.rut = rut_paciente
        self.primer_nombre = primer_nombre
        self.apellido_paterno = apellido_paterno
        self.edad = edad
        self.presupuesto = presupuesto
        self.prevision = prevision
    def __str__(self):
        return f"{self.rut} \n {self.primer_nombre} {self.apellido_paterno} \n {self.edad} \n {self.prevision}"
    '''
    Crea un método que permita identificar si es que el paciente es o no mayor de edad debe devolver verdadero cuando su edad es mayor o igual a 18 o falso un caso contrario
    '''
    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False

paciente1 = Paciente("1-9", "Ignacia", "silva", 80, 250000)
paciente2 = Paciente("18123456-0", "Carmen", "González", 12, 2000000, "Nueva Más vida")
paciente3 = Paciente("2-7", "Benjamín", "Silva", 18, 650000, "Consalud")

print(f"El paciente: {paciente1.primer_nombre}, tiene la previsión de:{paciente1.prevision}")
print(paciente2.prevision)
print(f"El paciente: {paciente2.primer_nombre} es mayor de edad??")
print(f"{paciente2.es_mayor_edad()}")
print(f"ya que el paciente tiene: {paciente2.edad} años")

pacientes = []

pacientes.append(paciente1)
pacientes.append(paciente2)
pacientes.append(paciente3)

for paciente in pacientes:
    print(paciente)

import matplotlib.pyplot as plt

'''
nombres = ["Ana", "Carmen", "Pamela"]
presupuestos = [5000000, 2000000, 7000000]

plt.bar(nombres, presupuestos)
plt.title("Presupuestos Pacientes")
plt.xlabel("Pacientes")
plt.ylabel("Presupuesto")

plt.show()
'''

nombres = []
presupuestos = []

for paciente in pacientes:
    nombres.append(paciente.primer_nombre + " " + paciente.apellido_paterno)
    presupuestos.append(paciente.presupuesto)

plt.bar(nombres, presupuestos)

plt.title("Gráfico de presupuesto disponible")
plt.xlabel("Pacientes")
plt.ylabel("Presupuesto")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

'''
Actividades
Ejecuta el gráfico con cinco pacientes.
Cambia rotation=45 por rotation=0.
Compara cuál gráfico se lee mejor.
Verifica que los nombres del eje X correspondan a los pacientes.
Verifica que los valores del eje Y correspondan a sus presupuestos.
'''
plt.plot(nombres, presupuestos, marker="o")

plt.title("Presupuesto disponible por paciente")
plt.xlabel("Pacientes")
plt.ylabel("Presupuesto")
plt.tight_layout()

plt.show()

mayores = 0
menores = 0
for objetoPaciente in pacientes:
    if objetoPaciente.es_mayor_edad():
        mayores += 1
    else:
        menores += 1

etiquetas = ["Mayores de edad", "Menores de edad"]
valores = [mayores, menores]

plt.pie(valores, labels=etiquetas, autopct="%1.1f%%")
plt.title("Distribución de pacientes por mayoría de edad")
plt.show()


'''
Tarea Pa' la casa:

Construye un programa que tenga:

Una clase Paciente.
Constructor __init__.
Método obtener_nombre_completo().
Método es_mayor_edad().
Método tiene_presupuesto_suficiente(costo).
Método puede_agendar(costo).
Método __str__().
Una lista con al menos cinco pacientes.
Un gráfico de barras con el presupuesto disponible de los pacientes.
Un gráfico circular con la cantidad de mayores y menores de edad.

'''


