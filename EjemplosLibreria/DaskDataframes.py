import dask.dataframe as dd

# Leer un archivo CSV grande en un DataFrame de Dask
df = dd.read_csv('datos_grandes.csv')

# Filtrar filas y calcular el promedio de una columna
resultado = df[df['columna'] > 100]['columna'].mean()

# Ejecutar el cálculo
media = resultado.compute()

print("Media de los valores mayores a 100:", media)
