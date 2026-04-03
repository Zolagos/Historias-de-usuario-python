#nombre,precio,cantidad

#Una funcion para agregar productos al inventario
def agregar_producto():
    nuevo_producto ={
        "nombre":nombre, 
        "precio":precio, 
        "cantidad":cantidad
        }
    inventario.append(nuevo_producto)
    print(f"\n✅ Producto '{nombre}' agregado correctamente.")
    

#una funcion para mostar el inventario que se tiene
def mostrar_inventario():
    if not inventario:
        print("\n[!] El invemtario esta vacio.")
        return
    #Se utiliza para que los datos salgan tipo tabla
    print("\n" + "=" * 50)
    print(f" {'Nombre del producto':<20} | {'Precio':>10} | {'Cant.':>6}")
    print("=" * 50)

    for datos in inventario:
        nombre = datos["nombre"]
        precio = datos["precio"]
        cantidad = datos["cantidad"]
        #Se utiliza para que los datos salgan tipo tabla
        print(f" {nombre:<20} | {precio:>10.2f} | {cantidad:>6}")
    print("=" * 50 + "\n")

#Una funcion para mostar las estadisticas del valor total y la cantidad total
def calcular_estadistica():
    suma_valor_total = 0
    suma_cantidad = 0
    for producto in inventario:
        cantidad = producto['cantidad']
        precio = producto['precio']
        suma_cantidad += cantidad
        valor_total = precio * cantidad
        suma_valor_total += valor_total
    estadistica = {
        'valor total':suma_valor_total,
        'cantidad total':suma_cantidad
    }
#Imprimir los datos solicitados, se utiliza para que los datos salgan tipo tabla
    print(f" {'Estadistica':<20} | {'Valor'}")
    print("=" * 40)
    for est, valor in estadistica.items():
        print(f" {est:<20} | {valor}")
    print("=" * 40 + "\n") 


#Ciclo while para seguir preguntando el precio mientras no den un valor valido.
menu = ""
inventario = []
while menu !="4":
    menu = input("Eliga una opcion:\n 1.Agregar producto\n 2.Mostrar inventario\n " \
    "3.Calcular estadisticas\n 4.Salir\n")
    if menu == "1":
        try:
            nombre = input("Digite el nombre del producto: ")
            precio = float(input("Digite el precio del producto: "))
            if precio <= 0:
                raise ValueError
            cantidad = int(input("Digite la cantidad del producto: "))
            if precio <= 0:
                raise ValueError
            agregar_producto()
        except ValueError:
            print("Dato invalido")
    if menu == "2":
        mostrar_inventario()
    if menu == "3":
        calcular_estadistica()
    if menu == "4":
        print("Saliendo del inventario.")
 
# Control de flujo y manejo de listas en el inventario, se le muestra al usuario un menu donde puede
# eleir entre agregarproducto, mostrar producto, calcular las estadisticas y salir.