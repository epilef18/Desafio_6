"""Menú visual de Pizza JAT
    Contiene una visual en ascii con el logo de la empresa y un menú visual con las opciones posibles para que el cliente interactue con el programa y haga su pedido
    Variables: No contiene
    
    Returns: input[seleccion]: Registra las elecciones del cliente para ser procesadas en los otros programas.
    """
def mostrar_menu():
    print(r"   _____ _                     _      _______   ")
    print(r"  |  __ (_)                   | |  /\|__   __|  ")
    print(r"  | |__) | __________ _       | | /  \  | |     ")
    print(r"  |  ___/ |_  /_  / _` |  _   | |/ /\ \ | |     ")
    print(r"  | |   | |/ / / / (_| | | |__| / ____ \| |     ")
    print(r"  |_|   |_/___/___\__,_|  \____/_/    \_\_|     ")
    print("------------BIENVENIDO A PIZZA JAT---------------")
    print("Por favor, seleccione una opción:")
    print("1. Seleccionar masa")
    print("2. Seleccionar salsa")
    print("3. Seleccionar ingredientes")
    print("4  Mostrar ingredientes seleccionados")
    print("5. Tiempo de entrega y confirmar Pedido")
    print("6. Salir")
    return int(input("¿Qué opcion desea?:"))

    
                                             
                                             