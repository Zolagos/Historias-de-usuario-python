#Solicitar datos al usuario
nombre = str(input("Ingrese el nombre del producto: "))

#Ciclo while para seguir preguntando el precio mientras no den un valor valido
op = False
while not op:
    try:
        #Solicitar datos al usuario
        precio = float(input("Digite el precio: "))
        op = True
    except:
        print("Digite un valor valido")


#Ciclo while para seguir preguntando la cantidad mientras no den un valor valido
op = False
while not op:
    try:
        #Solicitar datos al usuario
        cantidad = int(input("Digite la cantidad: "))
        op = True
    except:
        print("Digite un valor valido")

#Operacion matematica
costo_total = precio * cantidad

#Imprimir los datos solicitados
print(
    f"Producto:{nombre}",
    f"Precio:{precio}",
    f"Cantidad:{cantidad}",
    f"Total:{costo_total}",
    sep="\n"
)

#Se le solicita al usuario que digite el nombre del producto, el precio y la cantidad.
#Se realiza una operacion matematica para saber el costo total y se le muestra un resumen de las variable al usuario