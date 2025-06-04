# Nombre: Cruz Eduardo Gamez Rodriguez
# Registro: 21110301

# Se crea una lista desordenada que será ordenada de menor a mayor.
lista = [6, 8, 2, 3, 1, 9, 4, 7, 5]

# Se obtiene la longitud de la lista para utilizarla en los bucles.
longitud = len(lista)

# Ciclo externo: recorre la lista desde el primer elemento hasta el penúltimo.
for i in range(longitud - 1):
    # Muestra el estado actual de la lista antes de hacer el cambio en esta iteración.
    print(lista)
    
    # Inicializa la posición del número menor con el índice actual.
    menor = i
    print("El número menor a evaluar actualmente está en la posición:", menor)
    
    # Ciclo interno: recorre desde el siguiente elemento hasta el final de la lista.
    for j in range(i + 1, longitud):
        # Compara el elemento actual con el más pequeño encontrado.
        if lista[j] < lista[menor]:
            # Si encuentra uno más pequeño, actualiza la posición del menor.
            menor = j
            print("Nuevo número menor encontrado en la posición:", menor)
    
    # Realiza el intercambio entre el número en la posición actual y el menor encontrado.
    temp = lista[menor]     # Guarda temporalmente el valor del menor.
    lista[menor] = lista[i] # Asigna el valor actual en la posición del menor.
    lista[i] = temp         # Asigna el menor al lugar original del valor actual.
    
    # Muestra qué valores se intercambiaron.
    print(f"Se cambia el número: {lista[menor]} con: {lista[i]}")

# Imprime la lista ya ordenada de menor a mayor.
print("Lista final ordenada:", lista)
