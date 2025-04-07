# ---------------------------------Problem csv-----------------------------------------

# Cambiar el type de dato de una columna.
import pandas as pd

df = pd.read_csv("exercises\\files\\csv\\problem_csv.csv")

# Cambiando el tipo de dato de la columna "age" de int a str.
df["age"] = df["age"].astype(str)

# print(df)
# print(type(df["age"][0]))

# Remplazar un dato en una sola columna.
df["name"].replace("andres", "Andres...", inplace=True)

# Remplazar un dato en todas las columnas.
df.replace("ramirez", "Ramirez...", inplace=True)

# Para eliminar filas con datos faltantes.
df = df.dropna()

# Para eliminar filas repetidas.
df = df.drop_duplicates()

# Create un csv con el df result (limpio).
df.to_csv("exercises\\files\\csv\\problem_csv_result.csv")