from dask.distributed import Client
import time

# Iniciar un cliente local de Dask
client = Client()

# Función que tarda en ejecutarse
def trabajo_lento(x):
    time.sleep(1)
    return x * 2

# Enviar tareas al clúster como Futures
fut1 = client.submit(trabajo_lento, 10)
fut2 = client.submit(trabajo_lento, 20)

# Obtener los resultados (espera si no han terminado)
res1 = fut1.result()
res2 = fut2.result()

print("Resultados:", res1, res2)
