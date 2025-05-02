import dask.array as da

# Crear un array de Dask a partir de datos aleatorios
# 10000x10000 dividido en bloques de 1000x1000
x = da.random.random((10000, 10000), chunks=(1000, 1000))

# Realizar una operación: media de todos los valores
mean = x.mean()

# Ejecutar el cálculo
result = mean.compute()

print("Media:", result)
