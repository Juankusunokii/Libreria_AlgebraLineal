# Contador de Palabras en Archivos Grandes con Dask
Este es un proyecto hecho en python cuyo proposito es ser un contador de palabras en archivos muy grandes usando la biblioteca dask gracias a su procesamiento en paralelo 

# ¿Qué es Dask?
Dask es una biblioteca de Python diseñada para la computación paralela y el procesamiento de grandes volúmenes de datos que no caben en memoria. Ofrece estructuras de datos similares a pandas, NumPy y scikit-learn, pero divide las operaciones en pequeñas tareas que pueden ejecutarse de forma distribuida en múltiples hilos, procesos o incluso máquinas.

#Funciones
-Contador de palabras dentro del texto de manera rapida y eficaz
-Omision de palabras muy presentes en los textos como pueden ser "el , la , de , y , etc ".
( el usuario puede añadir mas palabras a ser omisas)
-Crea un top de palabras que mas aparecen en el texto. 
( el numero de puestos del top lo elige el usuario)


