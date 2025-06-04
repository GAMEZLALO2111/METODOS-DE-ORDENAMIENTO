# Nombre: Cruz Eduardo Gamez Rodriguez
# Registro: 21110301

# Lista desordenada que se desea ordenar usando el algoritmo QuickSort.
lista = [20, 2, 15, 16, 8, 1, 7, 11, 3, 9, 4, 5, 10, 6, 12, 14, 19, 13, 17, 19, 18]

# Función auxiliar que realiza la partición de la lista alrededor de un pivote.
def particionado(lista):
    # Se elige el primer elemento como pivote.
    pivote = lista[0]

    # Inicializa dos listas vacías para guardar elementos menores y mayores al pivote.
    menores = []
    mayores = []

    # Recorre la lista desde el segundo elemento (índice 1).
    for i in range(1, len(lista)):
        # Si el elemento actual es menor al pivote, se agrega a la lista 'menores'.
        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            # Si es mayor o igual, se agrega a la lista 'mayores'.
            mayores.append(lista[i])
    
    # Muestra cómo se dividió la lista con base en el pivote.
    print(f"Dividiendo lista: {lista}")
    print(f"Menores: {menores}, Pivote: {pivote}, Mayores: {mayores}")
    
    # Devuelve las listas 'menores', el 'pivote' y 'mayores'.
    return menores, pivote, mayores

# Función principal del algoritmo QuickSort.
def quicksort(lista):
    # Caso base: si la lista tiene menos de 2 elementos, ya está ordenada.
    if len(lista) < 2:
        return lista

    # Se divide la lista en menores, pivote y mayores mediante la función particionado.
    menores, pivote, mayores = particionado(lista)

    # Ordena recursivamente la lista de menores y de mayores, y las concatena con el pivote en el centro.
    resultado = quicksort(menores) + [pivote] + quicksort(mayores)

    # Muestra cómo se va construyendo la lista ordenada en cada paso recursivo.
    print(f"Unificando: {resultado}")
    
    # Retorna la lista ordenada resultante.
    return resultado

# Llama a la función quicksort con la lista original y muestra el resultado final ordenado.
print("\nLista ordenada final:", quicksort(lista))
