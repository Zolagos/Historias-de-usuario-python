"""
agregar_producto(inventario, nombre, precio, cantidad)
mostrar_inventario(inventario)
buscar_producto(inventario, nombre) → retorna el dict o None
actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
eliminar_producto(inventario, nombre)
calcular_estadisticas(inventario) → retorna tupla/dict con métricas
"""


def agregar_producto(inventario: list[dict[str,float|str|int]], nombre:str, precio:float, cantidad:int):
    """
    La funcion agrega productos al inventario
    Inventario: list 
    nombre: str
    precio: float
    cantidad: int

    """
    nuevo_producto ={
        "nombre":nombre, 
        "precio":precio, 
        "cantidad":cantidad
        }
    inventario.append(nuevo_producto)
    print(f"\n✅ Producto '{nombre}' agregado correctamente.")

def mostrar_inventario(inventario: list[dict[str,float|str|int]]):
    """
    La funcion muestra el inventario actual
    inventario: list

    """
    if not inventario:
        print("\n[!] El invemtario esta vacio.")
        return
    print("\n" + "=" * 50)
    print(f" {'Nombre del producto':<20} | {'Precio':>10} | {'Cant.':>6}")
    print("=" * 50)

    for datos in inventario:
        nombre = datos["nombre"]
        precio = datos["precio"]
        cantidad = datos["cantidad"]
        print(f" {nombre:<20} | {precio:>10.2f} | {cantidad:>6}")
    print("=" * 50 + "\n")


def buscar_producto(inventario: list[dict[str,float|str|int]], nombre:str) -> dict|None:
    """
    Inventario: list 
    nombre: str

    La funcion retorna el producto encontrado
    return:
    
    dict | none
    """

    for producto in inventario:
        if producto ['nombre'] == nombre:
            return producto
    return  None
        

def actualizar_producto(inventario: list[dict[str,float|str|int]], nombre:str, nuevo_precio=None, nueva_cantidad=None):
    producto = buscar_producto(inventario,nombre)
    if producto:
        producto['precio'] = nuevo_precio
        producto['cantidad'] = nueva_cantidad
        print(f"🔄 '{nombre}' actualizado.")
    else:
        print("❌ Error: Producto no encontrado.")

def eliminar_producto(inventario: list[dict[str,float|str|int]], nombre:str):
    producto = buscar_producto(inventario,nombre)
    if producto:
        inventario.remove(producto)
        print(f"🗑️ '{nombre}' ha sido eliminado.")
    else:
        print("❌ Error: No se pudo eliminar el producto.")

def calcular_estadisticas(inventario:list[dict[str,float|str|int]]):
    suma_cantidad = 0
    suma_valor_total = 0
    producto_mas_caro = 0
    producto_mayor_stock = 0
    nombre_producto_mas_caro = ""
    nombre_producto_mayor_stock = ""
    for producto in inventario:
        cantidad = producto['cantidad']
        precio = producto['precio']
        nombre = producto['nombre']
        suma_cantidad += cantidad
        valor_total = precio * cantidad
        suma_valor_total += valor_total
        if precio > producto_mas_caro:
            nombre_producto_mas_caro = nombre
            producto_mas_caro = precio
        if cantidad > producto_mayor_stock:
            nombre_producto_mayor_stock = nombre
            producto_mayor_stock = cantidad

    estadistica = {
        "suma cantidad":suma_cantidad,
        'valor total':suma_valor_total,
        'producto mas caro':(nombre_producto_mas_caro,producto_mas_caro),
        'producto con mayor stock':(nombre_producto_mayor_stock,producto_mayor_stock)
    }

    print(f" {'Estadistica':<20} | {'Valor'}")
    print("=" * 40)
    for est, valor in estadistica.items():
        print(f" {est:<20} | {valor}")
    print("=" * 40 + "\n")


