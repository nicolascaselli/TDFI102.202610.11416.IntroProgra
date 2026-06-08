opcion = 0

while opcion != 4:
    print("MENU")
    print("1. Problema 1 - Eventos")
    print("2. Problema 2 - Prestamo")
    print("3. Problema 3 - Ladrillos")
    print("4. Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        #acá va la mi respuesta del ejercicio 1

    elif opcion == 2:
        capital = float(input("Ingrese capital solicitado: "))
        meses = int(input("Ingrese cantidad de meses: "))

        if capital < 5000000:
            tasa = 0.04
        else:
            tasa = 0.03

        interes = capital * tasa * meses
        total = capital + interes

        print("Capital solicitado:", capital)
        print("Interes generado:", interes)
        print("Total a pagar:", total)

    elif opcion == 3:
        largo = float(input("Ingrese largo del muro: "))
        alto = float(input("Ingrese alto del muro: "))

        area = largo * alto
        ladrillos = area * 50

        if area > 2000:
            costo_ladrillo = 300
        else:
            costo_ladrillo = 350

        costo_final = ladrillos * costo_ladrillo

        print("Total de ladrillos necesarios:", ladrillos)
        print("Costo final:", costo_final)

    elif opcion == 4:
        print("Vuelva pronto")

    else:
        print("Opcion invalida")
