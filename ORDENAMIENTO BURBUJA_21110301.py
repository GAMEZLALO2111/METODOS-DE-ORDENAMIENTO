# Nombre: Cruz Eduardo Gamez Rodriguez
# Registro: 21110301

# Lista desordenada que se desea ordenar utilizando el método de burbuja (Bubble Sort).
lista = [5, 8, 7, 9, 3, 2, 1, 6, 4]

# Bucle externo: controla la cantidad de pasadas necesarias para ordenar completamente la lista.
for i in range(len(lista) - 1):
    # Bucle interno: compara elementos adyacentes y los intercambia si están en el orden incorrecto.
    for j in range(len(lista) - 1):
        # Muestra los elementos que se están comparando actualmente.
        print(f"Comparando: {lista[j]} con: {lista[j+1]}")
        
        # Si el elemento actual es mayor que el siguiente, se realiza un intercambio.
        if lista[j] > lista[j + 1]:
            # Intercambia los valores para colocarlos en el orden correcto.
            lista[j], lista[j + 1] = lista[j + 1], lista[j]
            
            # Muestra el intercambio realizado.
            print(f"Intercambiando: {lista[j]} por: {lista[j+1]}")
            
            # Alternativa con variable temporal (comentada).
            # temporal = lista[j]
            # lista[j] = lista[j+1]
            # lista[j+1] = temporal

# Muestra la lista completamente ordenada después de aplicar el algoritmo de burbuja.
print('La lista ya acomodada, dado los valores iniciales, termina siendo así:', lista)
