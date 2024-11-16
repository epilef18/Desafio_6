# Pizza JAT - Prototipo de Personalización de Pizzas

Este proyecto es un prototipo interactivo para Pizza JAT, una pizzería mundial, que busca automatizar su proceso de solicitud de pizzas. Este programa permite a los usuarios personalizar sus pizzas, calcular el tiempo estimado de preparación y gestionar su orden.

---

## Características

### 1. Personalización de Pizzas
El programa ofrece un menú interactivo que permite al usuario:
- **Seleccionar el tipo de masa**:
  - Masa Tradicional
  - Masa Delgada
  - Masa con Bordes de Queso
- **Seleccionar el tipo de salsa**:
  - Salsa de Tomate
  - Salsa Alfredo
  - Salsa Barbecue
  - Salsa Pesto
- **Agregar o eliminar ingredientes**:
  - Ingredientes disponibles:
    - Tomate
    - Champiñones
    - Aceitunas
    - Cebolla
    - Pollo
    - Jamón
    - Carne
    - Tocino
    - Queso

### 2. Estimación del Tiempo de Preparación
- **Tiempo base**: 20 minutos.
- **Tiempo adicional**: 2 minutos por cada ingrediente añadido (excluyendo masa y salsa).
- Posibilidad de confirmar el pedido después de mostrar el tiempo estimado.

### 3. Flujo del programa

- Inicia listas de ingredientes vacíos
- Mostrar menú interactivo
- Input para que el usuario ingrese sus opciones
- Muestra opciones disponibles
- Recibe por input la opción deseada
- Ejecuta la función requerida 
- Retorna el valor del pedido a las listas vacías

### 4. Programas incluidos

- main.py: Controla el flujo del programa y ejecuta las funciones requeridas
- menu.py: Menú interactivo con las acciones disponibles para el usuario
- estimaryconfirmar.py: Estima el tiempo total de espera por el pedido y confirma el pedido
- personalizarpizza.py: Contiene las funciones para personalizar la pizza; elegir masa, salsa, ingredientes(agregar y eliminar) y mostrar ingredientes añadidos

### 5. Funciones incluidas

- personalizarpizza.py:
    - elegir_masa: Muestra las opciones de salsa y guarda la elección del usuario 
    - elegir_salsa: Muestra las opciones de masa y guarda la elección del usuario
    - seleccionar_ingredientes: Muestra las opciones de ingredientes, da la opción de agregar y eliminar ingredientes y guarda las elecciones del usuario
    - mostrar_ingredientes_act: Muestra los ingredientes seleccionados de la pizza
- estimaryconfirmar.py:
    - estimar_confirmar: Calcula el tiempo de preparación del pedido y permite confirmarlo o cancelarlo
- menu.py:
    - mostrar_menu: Muestra el logo de Pizza JAT y muestra las opciones de acción al usuario
  
### 6. Programas requeridos
  - Python 3.12 o más reciente
    
### 7. Cómo utilizar
  - Clona este repositorio
  - Usando la terminal, abre la carpeta contenedora e inicializa el programa main usando "python main.py"
