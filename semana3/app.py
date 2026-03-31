#nombre": str, "precio": float, "cantidad": int}
from servicios import *

inventario = {1:{"nombre":"lapiz", "precio":2000, "cantidad":2}}
nombre = input("Digite el nombre del producto: ")
precio = float(input("Digite el precio del producto: "))
cantidad = int(input("Digite la cantidad del producto: "))

agregar_producto(inventario, nombre, precio, cantidad)
print(inventario)
