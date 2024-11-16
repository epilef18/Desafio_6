from menu import mostrar_menu
from estimaryconfirmar import estimar_confirmar
from personalizarpizza import elegir_masa, elegir_salsa, seleccionar_ingredientes, mostrar_ingredientes_act

masa=""
salsa=""
ingredientes_act = []

while True:
    opcion = mostrar_menu()

    if opcion == 1:
        m = elegir_masa()
        print(f"Elegiste la masa {m}")
    elif opcion == 2:
        s = elegir_salsa()
        print(f"Elegiste la salsa {s}")
    elif opcion == 3:
        ingredientes_act = seleccionar_ingredientes(ingredientes_act)
    elif opcion == 4:
        mostrar_ingredientes_act(ingredientes_act)
    elif opcion == 5:
        estimar_confirmar(ingredientes_act)
    elif opcion == 6:
        print("Gracias por preferir Pizza JAT!")
    else:
        print("Opción inválida. Ingresa una opción Válida [1, 2, 3, 4, 5, 6]")

if __name__ == "__main__":
    main()