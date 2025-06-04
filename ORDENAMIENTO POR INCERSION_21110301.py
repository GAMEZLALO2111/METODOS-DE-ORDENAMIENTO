# Nombre: Cruz Eduardo Gamez Rodriguez
# Registro: 21110301

# Lista desordenada que se desea ordenar usando el algoritmo de inserción.
lista = [6, 8, 2, 3, 1, 9, 4, 7, 5]

# Muestra la lista original antes de iniciar el ordenamiento.
print("Lista inicial:", lista)

# Ciclo externo que recorre cada elemento a partir del segundo (índice 1).
for i in range(1, len(lista)):
    # Se guarda el valor del elemento actual que se va a insertar.
    actual = lista[i]
    
    # Índice auxiliar que se utilizará para comparar hacia la izquierda.
    indice = i

    # Muestra información del inicio de la iteración actual.
    print(f"\nIteración {i}:")
    print(f"Elemento actual: {actual}")

    # Ciclo que desplaza hacia la derecha los elementos mayores al actual.
    while indice > 0 and lista[indice - 1] > actual:
        # Muestra comparación entre el elemento anterior y el actual.
        print(f"Comparando {lista[indice - 1]} > {actual}: Sí")
        
        # Desplaza el elemento hacia la derecha.
        lista[indice] = lista[indice - 1]
        
        # Actualiza el índice para seguir comparando hacia la izquierda.
        indice -= 1
        
        # Muestra cómo va quedando la lista tras cada desplazamiento.
        print("Estado actual de la lista:", lista)

    # Inserta el valor actual en su posición correcta.
    lista[indice] = actual

    # Muestra información de la inserción.
    print(f"Insertado {actual} en posición {indice}")
    print("Lista después de esta iteración:", lista)

# Al finalizar, se muestra la lista completamente ordenada.
print("\nLista ordenada:", lista)
