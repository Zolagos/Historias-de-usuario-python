"""
agregar_producto(inventario, nombre, precio, cantidad)
mostrar_inventario(inventario)
buscar_producto(inventario, nombre) → retorna el dict o None
actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
eliminar_producto(inventario, nombre)
calcular_estadisticas(inventario) → retorna tupla/dict con métricas
"""

cont = 1

def agregar_producto(inventario, nombre, precio, cantidad):
    global cont
    cont+=1
    inventario[cont]={"nombre":nombre, "precio":precio, "cantidad":cantidad}

def mostrar_inventario(inventario):
    print(inventario)
    #buscar para que se vea mejor

def buscar_producto(inventario, nombre):
    for llave, clave in inventario.items():
        if clave.get