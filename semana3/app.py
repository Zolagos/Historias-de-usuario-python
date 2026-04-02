#nombre": str, "precio": float, "cantidad": int}
from servicios import *



inventario =[]
opcion = ""
while opcion != "9":
    print("=" * 40)
    print(" 📦 SISTEMA DE GESTIÓN DE INVENTARIO 📦")
    print("=" * 40)
    print("  [1] Agregar producto")
    print("  [2] Mostrar inventario")
    print("  [3] Buscar producto")
    print("  [4] Actualizar producto")
    print("  [5] Eliminar producto")
    print("  [6] Estadísticas del inventario")
    print("  [7] Guardar datos en CSV")
    print("  [8] Cargar datos desde CSV")
    print("  [9] Salir")
    print("=" * 40) 
    opcion = input("👉 Seleccione una opción (1-9): ")
    if opcion == "1":
        try:
            nombre = input("Digite el nombre del producto: ")
            precio = float(input("Digite el precio del producto: "))
            if precio <= 0:
                raise ValueError
            cantidad = int(input("Digite la cantidad del producto: "))
            if precio <= 0:
                raise ValueError
            agregar_producto(inventario, nombre, precio, cantidad)
        except ValueError:
            print("Dato invalido")
    if opcion == "2":
        mostrar_inventario(inventario)
    if opcion == "3":
        nombre = input("Digite el nombre del producto: ")
        producto = buscar_producto(inventario, nombre)
        if producto:
                print(f"\n✅ Encontrado: {producto['nombre']} | ${producto['precio']} | Stock: {producto['cantidad']}")
        else:
                print("\n❌ Producto no encontrado.")
    if opcion == "4":
        try:
            nombre = input("Digite el nombre del producto a actualizar: ")
            precio = float(input("Digite el nuevo precio del producto: "))
            if precio <= 0:
                raise ValueError
            cantidad = int(input("Digite la nueva cantidad del producto: "))
            if precio <= 0:
                raise ValueError
            actualizar_producto(inventario, nombre, nuevo_precio=precio, nueva_cantidad=cantidad)
        except ValueError:
            print("Dato invalido")
    if opcion == "5":
        nombre = input("Digite el nombre del producto: ")
        eliminar_producto(inventario, nombre)
    if opcion == "6":
        calcular_estadisticas(inventario)




