import dask.bag as db
import string

# Lista de palabras comunes a ignorar
STOPWORDS = {"el", "la", "de", "y", "en", "que", "a", "los", "las", "un", "una"}

def leer_archivo(path):
    """Lee el archivo de texto en un Dask Bag."""
    return db.read_text(path)

def limpiar_linea(linea):
    """Limpia una línea de texto: elimina puntuación y pasa a minúsculas."""
    translator = str.maketrans('', '', string.punctuation)
    return linea.translate(translator).lower()

def contar_palabras(bag):
    """Cuenta las palabras en el Dask Bag."""
    palabras = bag.map(limpiar_linea).flat_map(lambda linea: linea.split())
    return palabras.frequencies()

def filtrar_stopwords(frecuencias, stopwords):
    """Filtra palabras que estén en la lista de stopwords."""
    return frecuencias.filter(lambda x: x[0] not in stopwords)

def mostrar_top(frecuencias, n=10):
    """Muestra las top n palabras más comunes."""
    top = frecuencias.topk(n, key=lambda x: x[1])
    print("\nTop palabras más comunes:\n")
    for palabra, cantidad in top.compute():
        print(f"{palabra}: {cantidad}")

def agregar_stopwords(palabras_extra):
    """Agrega palabras nuevas a las stopwords."""
    nuevas = {p.strip().lower() for p in palabras_extra.split(",")}
    return STOPWORDS.union(nuevas)

# --- Programa Principal ---

if __name__ == "__main__":
    print("=== Contador de Palabras ===\n")

    archivo = input("Ingrese el nombre del archivo de texto a analizar: ").strip()
    try:
        bag = leer_archivo(archivo)
    except Exception as e:
        print(f"Error al abrir el archivo: {e}")
        exit()

    agregar = input("\n¿Desea agregar palabras adicionales a ignorar? (s/n): ").lower()
    stopwords_activas = STOPWORDS
    if agregar == "s":
        palabras_extra = input("Ingrese palabras separadas por comas (ej: esto,eso,aquel): ")
        stopwords_activas = agregar_stopwords(palabras_extra)

    try:
        n = int(input("\n¿Cuántas palabras desea mostrar en el ranking?: "))
    except ValueError:
        print("Número inválido, mostrando top 10 por defecto.")
        n = 10

    frecuencias = contar_palabras(bag)
    frecuencias_filtradas = filtrar_stopwords(frecuencias, stopwords_activas)
    mostrar_top(frecuencias_filtradas, n=n)
