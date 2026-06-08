nombre = "Camila"
apellido = "Rojas"
edad = 19
carrera = "Ingeniería Civil Informática"
nota_final = 5.8

print(nombre)
print(apellido)
print(edad)
print(carrera)
print(nota_final)


estudiante = {
    "nombre": "Camila",
    "apellido": "Rojas",
    "edad": 19,
    "carrera": "Ingeniería Civil Informática",
    "nota_final": 5.8
}


print(estudiante["nombre"])
print(estudiante["nota_final"])

'''
atributos:
    - nombre
    - apellido
    - edad
    - carrera
    - seccion
    - nota_final
'''
class Estudiante:
    def __init__(self, nombre, apellido, edad, carrera, seccion, nota_final):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.carrera = carrera
        self.seccion = seccion
        self.nota_final = nota_final

    def moastrarDatos(self):
        print(self.nombre)
        print(self.apellido)
        print(self.edad)
        print(self.carrera)
        print(self.seccion)
        print(self.nota_final)

    def estaAprobado(self):
        if self.nota_final >= 4:
            return True
        else:
            return False

estudiante1 = Estudiante("Camila", "Rojas", 19, "informática", "De industriales", 1)
estudiante2 = Estudiante("Pepito", "Paga doble", 20, "Industrial", "De industriales también", 3)


print(f"mostrando el método mostrarDatos:")
estudiante1.moastrarDatos()


'''
Necesitamos resolver de alguna forma, saber si un estudiante tiene el estado de reprobado o aprobado
'''
print(estudiante1.estaAprobado())

if estudiante1.estaAprobado() == False:
    print("El estudiante tiene el estado de reprobado")
    print("su nota final es de", estudiante1.nota_final)
