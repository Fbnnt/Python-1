#Fabian Vargas
# 26-04-2025
def agregar_producto(inventario, producto, cantidad):
    inventario[producto] = inventario.get(producto, 0) + cantidad

def eliminar_producto(inventario, producto):
    if producto in inventario:
        inventario.pop(producto)
    else:
        print(f"El producto '{producto}' no se encuentra en el inventario.")

def actualizar_cantidad(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] = cantidad
    else:
        print(f"No se puede actualizar. El producto '{producto}' no existe.")

def mostrar_inventario(inventario):
    if inventario:
        print("Inventario actual:")
        for producto, cantidad in inventario.items():
            print(f"{producto}: {cantidad}")
    else:
        print("El inventario está vacío.")

inventario = {}

agregar_producto(inventario, "Manzanas", 10)
agregar_producto(inventario, "Naranjas", 5)

mostrar_inventario(inventario)

actualizar_cantidad(inventario, "Manzanas", 15)

eliminar_producto(inventario, "Naranjas")

mostrar_inventario(inventario)
