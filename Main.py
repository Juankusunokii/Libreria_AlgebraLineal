import dask.dataframe as dd

# Leer múltiples archivos CSV (puedes usar comodines)
df = dd.read_csv('data/ventas_*.csv')

# Mostrar esquema de datos (sin cargar todo)
print("Columnas:", df.columns)
print("Tipos de datos:\n", df.dtypes)

# Limpiar datos: eliminar filas con valores nulos
df = df.dropna()

# Convertir columna de fechas si es necesario
df['fecha'] = dd.to_datetime(df['fecha'])

# Agregar: total de ventas por mes
df['mes'] = df['fecha'].dt.to_period('M')
ventas_mensuales = df.groupby('mes')['venta'].sum().compute()

print("Ventas por mes:")
print(ventas_mensuales)

# Filtrar ventas mayores a cierto umbral y guardar resultado
ventas_altas = df[df['venta'] > 10000]

# Guardar el resultado en CSVs separados por partición
ventas_altas.to_csv('resultados/ventas_altas_*.csv', index=False)
