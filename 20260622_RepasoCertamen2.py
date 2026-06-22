class Cliente:

    def __init__(self, rut, nombre, tipo, email, direccion, valor_total, telefono = None):
        self.rut = rut
        self.nombre = nombre
        self.tipo = tipo
        self.email = email
        self.direccion = direccion
        self.telefono = telefono
        self.valor_total = valor_total

    def mostrar_datos(self):
        print("RUT cliente:", self.rut)
        print("Nombre cliente:", self.nombre)
        print("Tipo de cliente:", self.tipo)
        print("Correo electrónico:", self.email)
        print("Dirección:", self.direccion)
        print("Valor total del paquete turístico:", self.valor_total)
        print("-" * 40)

    def mostrar_nombre_valor(self):
        print("Nombre cliente:", self.nombre)
        print("Valor total del paquete turístico:", self.valor_total)
        print("-" * 40)

def validar_tipo_cliente():
    tipo=input("Ingrese el tipo de cliente (Nacional, Internacional): ")
    while tipo != "Nacional" and tipo != "Internacional":
        print("El valor ingresado no es un tipo de cliente válido, inténtalo nuevamente...")
        tipo = input("Ingrese el tipo de cliente (Nacional, Internacional): ")
    return tipo

def validar_valor_total():
    valor = int(input("Valor total del paquete turístico: "))
    while valor <= 0:
        print("Valor total incorrecto, debe ser mayor a 0")
        valor = int(input("Valor total del paquete turístico: "))
    return valor

def ingresar_cliente():
    print("Ingresar datos del cliente...")
    rut = input("Ingrese rut: ")
    nombre = input("Ingrese nombre: ")
    tipo = validar_tipo_cliente()
    email = input("Ingrese email: ")
    direccion = input("Ingrese direccion: ")
    valor_total = validar_valor_total()

    obj_cliente = Cliente(rut, nombre, tipo, email, direccion, valor_total)
    return obj_cliente

def agregar_cliente(lista_clientes):
    obj_cliente = ingresar_cliente()
    lista_clientes.append(obj_cliente)
    print("Cliente agregado correctamente a la lista Clientes")

def visualizar_clientes(lista_clientes):
    if len(lista_clientes) == 0:
        print("Lista no tiene clientes agregados")
    else:
        print("Listando los clientes en lista:")
        for obj_cliente in lista_clientes:
            obj_cliente.mostrar_datos()

def mostrar_mayor_y_menor(lista_clientes):
    if len(lista_clientes) == 0:
        print("Lista no tiene clientes agregados")
        return

    cliente_mayor = lista_clientes[0]
    cliente_menor= lista_clientes[0]

    for obj_cliente in lista_clientes:
        if obj_cliente.valor_total > cliente_mayor.valor_total:
            cliente_mayor = obj_cliente

        if obj_cliente.valor_total < cliente_menor.valor_total:
            cliente_menor = obj_cliente

    print("Cliente con menor valor total del paquete turístico")
    print("RUT cliente:", cliente_menor.rut)
    print("Nombre cliente:", cliente_menor.nombre)
    print("Valor total del cliente:", cliente_menor.valor_total)

    print("Cliente con mayor valor total del paquete turístico")
    print("RUT cliente:", cliente_mayor.rut)
    print("Nombre cliente:", cliente_mayor.nombre)
    print("Valor total del cliente:", cliente_mayor.valor_total)

ARCHIVO_CLIENTES = "clientes.txt"
ARCHIVO_VALORES = "valores_paquetes.txt"

def guardar_cliente_archivo(obj_cliente):
    with open(ARCHIVO_CLIENTES, "a", encoding="utf-8") as archivo_cltes:
        linea_txt = f"{obj_cliente.rut}; {obj_cliente.nombre}; {obj_cliente.tipo};{obj_cliente.email};"
        linea_txt += f"{obj_cliente.direccion}; {obj_cliente.valor_total} \n"
        archivo_cltes.write(linea_txt)

    with open(ARCHIVO_VALORES, "a", encoding="utf-8") as archivo_values:
        archivo_values.write(str(obj_cliente.valor_total)+ "\n")

def cargar_clientes_archivo():
    lista_clientes = []

    try:
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas[1:]:
                datos = linea.strip().split(";")
                if len(datos) == 7:
                    rut = datos[0]
                    nombre = datos[1]
                    tipo = datos[2]
                    email = datos[3]
                    direccion = datos[4]
                    telefono = datos[5]
                    valor_total = int(datos[6])
                    obj_cliente = Cliente(rut, nombre, tipo, email, direccion, telefono, valor_total)
                    lista_clientes.append(obj_cliente)
    except FileNotFoundError:
        print("Archivo no encontrado, deberías crearlo o revisar la ruta...")
    return lista_clientes

def menu():
    lista_clientes = cargar_clientes_archivo()
    opcion = 0
    while opcion != 5:
        print("MENÚ")
        print("1. Ingresar datos de clientes")
        print("2. Visualizar datos de clientes")
        print("3. Visualizar Rut y Nombre del cliente con mayor y menor valor")
        print("4. Visualizar Nombre y valor total de cada cliente")
        print("5. Salir")
        opcion = int(input("Ingrese su opcion: "))

        if opcion == 1:
          obj_cliente = ingresar_cliente()
          lista_clientes.append(obj_cliente)
          guardar_cliente_archivo(obj_cliente)
          print("Cliente agregado correctamente a la lista Clientes")
        elif opcion == 2:
            visualizar_clientes(lista_clientes)
        elif opcion == 3:
            mostrar_mayor_y_menor(lista_clientes)
        elif opcion == 4:
            visualizar_clientes(lista_clientes)
        elif opcion == 5:
            print("Salir")
        else:
            print("Opcion no valida")

menu()