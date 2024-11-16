"""Permite calcular y mostrar el tiempo de espera del pedido listo. Luego da la opción de confirmar el pedido.

    Variables:
        ingredientes_act(arr): Ingredientes requeridos por el usuario.
        tiempo(int):Tiempo de espera del pedido
        confirmar(str): opción (y/n) para confirmar el pedido.
    
    Returns: salsas[seleccion-1]: Tipo de masa seleccionada por el usuario


    """
def estimar_confirmar(ingredientes_act):
    tiempo = 20 + (2*len(ingredientes_act))
    print(f'El tiempo estimado es de: {tiempo} minutos')
    confirmar = input("¿Desea confirmar su orden?:(y/n)")
    if confirmar == 'y':
        print('Su pedido ha sido confirmado.')
    elif confirmar == 'n':
        print('Su pedido ha sido cancelado.')
    else:
        print('Eliga una opcion valida (y/n)')