contador = 1

suma_invitados = 0
suma_monto_final = 0

cont_pequeno = 0
cont_mediano = 0
cont_grande = 0

while contador <= 10:
    print("Evento", contador)
    tipo = input("Ingrese tipo de evento (pequeno, mediano, grande): ")
    invitados = int(input("Ingrese cantidad de invitados: "))

    if tipo == "pequeno":
        monto_base = 200000
        cont_pequeno = cont_pequeno + 1
    elif tipo == "mediano":
        monto_base = 400000
        cont_mediano = cont_mediano + 1
    else:
        monto_base = 700000
        cont_grande = cont_grande + 1

    if invitados >= 50 and invitados <= 100:
        recargo = monto_base * 0.05
    elif invitados >= 101 and invitados <= 200:
        recargo = monto_base * 0.08
    elif invitados > 200:
        recargo = monto_base * 0.12
    else:
        recargo = 0

    monto_final = monto_base + recargo

    suma_invitados = suma_invitados + invitados
    suma_monto_final = suma_monto_final + monto_final

    contador = contador + 1

promedio_invitados = suma_invitados / 10
promedio_monto_final = suma_monto_final / 10

print("Promedio de invitados:", promedio_invitados)
print("Promedio de monto final:", promedio_monto_final)
print("Cantidad de eventos pequenos:", cont_pequeno)
print("Cantidad de eventos medianos:", cont_mediano)
print("Cantidad de eventos grandes:", cont_grande)
