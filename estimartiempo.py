
def estimar_confirmar(ingredientes_act):
    tiempo = 20 + (2*len(ingredientes_act))
    print(f'El tiempo estimado es de: {tiempo} minutos')
    confirmar = input("¿Desea confirmar su orden?:(y/n)")
    while confirmar == 'y':
        print('Su pedido ha sido confirmado.')
        if confirmar == 'n':
            print('Su pedido ha sido cancelado.')
        else:
            print('Eliga una opcion valida (y/n)')
            continue
        