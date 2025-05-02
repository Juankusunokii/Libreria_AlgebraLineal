from dask import delayed
import time

# Función simulada que tarda tiempo
def lento_suma(x, y):
    time.sleep(1)
    return x + y

# Crear tareas diferidas
a = delayed(lento_suma)(1, 2)
b = delayed(lento_suma)(3, 4)
c = delayed(lento_suma)(a, b)

# Ejecutar todo en paralelo (tomará ~2 segundos en lugar de 3)
resultado = c.compute()

print("Resultado:", resultado)
