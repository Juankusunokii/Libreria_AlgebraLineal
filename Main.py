import dask.array as da

# Crear dos matrices grandes de 4000x4000 divididas en bloques de 1000x1000
A = da.random.random((4000, 4000), chunks=(1000, 1000))
B = da.random.random((4000, 4000), chunks=(1000, 1000))

# Operaciones básicas
suma = A + B
resta = A - B
producto_elemento = A * B

# Producto matricial
producto_matriz = A @ B

# Transposición
transpuesta_A = A.T

# Estadísticas
media_A = A.mean()
max_B = B.max()
norma_A = da.linalg.norm(A)

# Ejecutar y mostrar los resultados
print("Media de A:", media_A.compute())
print("Máximo de B:", max_B.compute())
print("Norma de A:", norma_A.compute())

# Cuidado con matrices pequeñas si necesitas determinante o inversa:
# Ejemplo con una matriz 3x3
M = da.from_array([[1, 2, 3], [0, 1, 4], [5, 6, 0]], chunks=(3, 3))
determinante = da.linalg.det(M)
print("Determinante de M:", determinante.compute())/ventas_altas_*.csv', index=False)
