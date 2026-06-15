import pandas as pd
import matplotlib.pyplot as plt

#leer el archivo de pacientes (pacientes_300.csv)
df = pd.read_csv("pacientes_300.csv")
print(df)
print(f"Primeras filas del data frame (df):")
print(df.head())

print("Últimas filas:")
print(df.tail())

print("Cantidad de filas y columnas:")
print(df.shape)

print("Columnas:")
print(df.columns)
print("Tipos de datos:")
print(df.dtypes)

print(df[["primer_nombre", "apellido_paterno", "edad", "rut",  "presupuesto"]])

df["nombre_completo"] = df["primer_nombre"] + " " + df["apellido_paterno"]
print(df[["nombre_completo", "edad", "presupuesto"]])

print(df.columns)

df["es_mayor_de_edad"] = df["edad"] >= 18
print(df[["nombre_completo", "edad", "es_mayor_de_edad"]])

mayores = df[df["edad"]>=18]
print(mayores)
print(mayores[["primer_nombre", "apellido_paterno", "edad"]])
menores = df[df["edad"]<18]
print(menores)

resultado = df[df["presupuesto"] >= 5000000]
print(resultado)

resultado = df[(df["edad"]>=18) & (df["presupuesto"]>=3000000)]
print(resultado)
print(resultado[["primer_nombre", "apellido_paterno", "edad", "presupuesto"]])

print("Presupuesto promedio:", df["presupuesto"].mean())
print("Presupuesto máximo:", df["presupuesto"].max())
print("Presupuesto mínimo:", df["presupuesto"].min())
print("Edad promedio:", df["edad"].mean())

'''
Grafique el presupuesto de los primeros 10 pacientes del archivo.
import matplotlib.pyplot as plt
'''
primeros_10 = df.head(10)
plt.bar(primeros_10["nombre_completo"], primeros_10["presupuesto"])
plt.title("Primeros 10 pacientes del archivo")
plt.xlabel("Pacientes")
plt.ylabel("Presupuesto")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#datos ordenados por ppto decendentes
ordenado = df.sort_values(by="presupuesto", ascending=False)
top_10 = ordenado.head(10)
plt.bar(top_10["nombre_completo"], top_10["presupuesto"])
plt.title("10 pacientes con mayor presupuesto")
plt.xlabel("Pacientes")
plt.ylabel("Presupuesto")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

mayores = len(df[df["edad"] >= 18])
menores = len(df[df["edad"] < 18])

etiquetas = ["Mayores de edad", "Menores de edad"]
valores = [mayores, menores]
plt.pie(valores, labels=etiquetas, autopct="%1.1f%%")
plt.title("Distribución de pacientes por mayoría de edad")
plt.show()


