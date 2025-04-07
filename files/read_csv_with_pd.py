import pandas as pd

# para leer file .csv con pandas.
df = pd.read_csv("files\\file.csv")
# df2 = pd.read_csv("files\\file.csv")

# data generar del df.
# print(df)

# data ordenada por age, ascendente.
# print(df.sort_values(["age"]))

# data ordenada por age, descendente.
# print(df.sort_values(["age"], ascending=False))

# para obtener los datos de una columna.
# print(df["name"])

# concatenando los dos df.
# print(pd.concat([df, df2]))

# accediendo a las primeras 3 filas con head().
# print(df.head(3))

# accediendo a las ultimas 3 filas con head().
# print(df.tail(3))

# accediendo a la cantidad de filas y columnas con shape.
# print(df.shape)

# obteniendo data estadística del df.
# print(df.describe())

# accediendo a un dato especifico del df con loc.
# print(df.loc[0, "age"])

# accediendo a todas las columnas de una fila.
# print(df.loc[0,:])

# accediendo a un dato especifico del df con iloc.
# print(df.iloc[0, 2])

# accediendo a todas las filas de una columna.
# print(df.iloc[:,2])

# accediendo a todas las columnas de una fila.
# print(df.iloc[0,:])

# accediendo a filas donde la age sea mayor o igual que 26.
print(df.loc[df["age"] >= 26,:])