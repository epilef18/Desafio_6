def salsa():
    """Muestra y permite elegir el tipo de salsa.
    Variables:
        salsas(arr): contiene las opciones de masas disponibles
        seleccion(str):opcion ingresada por el usuario con formato de número entero
    
    Returns: salsas[seleccion-1]: Tipo de masa seleccionada por el usuario


    """
    salsas = ["Tomate", "Alfredo", "Barbecue", "Pesto"]

    for i, s in enumerate(salsas, 1):
        print(f"{i}. {s}")

    seleccion = int(input("Seleccione la salsa: "))

    return salsas[seleccion -1]


def masa():
    """Muestra y permite elegir el tipo de masa.
    Variables:
        masas(arr): contiene las opciones de masas disponibles
        seleccion(str):opcion ingresada por el usuario con formato de número entero
    
    Returns: masas[seleccion-1]: Tipo de masa seleccionada por el usuario
    """

    masas = ["Tradicional", "Delgada", "Bordes de Queso"]

    for i, m in enumerate(masas, 1):
        print(f"{i}. {m}")

    seleccion = int(input("Seleccione el tipo de masa: "))

    return masas[seleccion - 1]


def seleccionar_ingredientes(ingredientes_act):
    ingredientes = ["Tomate", "Champiñones", "Aceituna","Cebolla", "Pollo", "Jamon", "Carne", "Tocino", "Queso"]
    
    for i, ing in enumerate(ingredientes, 1):
        print(f"{i}. {ing}")
    
    accion = input("Desea agregar(A) o eliminar(E) ingredientes? (A/E)").lower()
    if accion == "a":
        seleccion = int(input("Seleccione el ingrediente para agregar:"))
        if ingredientes[seleccion -1] not in ingredientes_act:
            ingredientes_act.append(ingredientes[seleccion - 1])
        return ingredientes_act

    elif accion == "e":
        seleccion = int(input("Seleccione el ingrediente para agregar:"))
        if ingredientes[seleccion -1] not in ingredientes_act:
            ingredientes_act.remove(ingredientes[seleccion - 1])
        return ingredientes_act
    
def mostrar_ingredientes_act(ingredientes_act):
    print("\n Ingredientes actuales en la Pizza:")
    for i in ingredientes_act:
        print(f'- {i}')
    