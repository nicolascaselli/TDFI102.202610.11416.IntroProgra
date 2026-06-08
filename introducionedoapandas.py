import pandas as pd
import matplotlib.pyplot as plt

pacientes = [
    {
        "rut": "19056987-1",
        "primer_nombre": "Ana",
        "apellido_paterno": "Sepulveda",
        "edad": 20,
        "presupuesto": 5000000
    },
    {
        "rut": "18123456-0",
        "primer_nombre": "Carmen",
        "apellido_paterno": "González",
        "edad": 22,
        "presupuesto": 2000000
    },
    {
        "rut": "23020318-4",
        "primer_nombre": "Pamela",
        "apellido_paterno": "Acosta",
        "edad": 17,
        "presupuesto": 7000000
    }
]

#for paciente in pacientes:
#    print(paciente["primer_nombre"], paciente["apellido_paterno"], paciente["presupuesto"])

df = pd.DataFrame(pacientes)
print(df)

print(df["primer_nombre"])
print(df["presupuesto"])
print(df[["primer_nombre", "apellido_paterno", "presupuesto"]])

df["nombre_completo"] = df["primer_nombre"] + " " + df["apellido_paterno"]

print(df)

df.plot(
    x="nombre_completo",
    y="presupuesto",
    kind="bar"
)
plt.show()