def guardar_csv(inventario, ruta, incluir_header=True):
        with open(ruta,'w',encoding='utf-8') as archivo:
                
                if incluir_header:
                        prod:dict = inventario[0]

                        cabecera = ','.join(prod.keys())
                        archivo.write(cabecera+'\n')

                for producto in inventario:
                    nombre = producto['nombre']
                    precio = producto['precio']
                    cantidad = producto['cantidad']
                    
                    archivo.write(f'{nombre},{precio},{cantidad}\n')


def cargar_csv(ruta):
        inventario = []
        errores = 0
        try:
           with open(ruta,mode='r',encoding='utf-8') as archivo:
                contenido = archivo.readlines()
                encabezado = contenido[0]
                encabezado = encabezado.strip().lower()
                datos = contenido[1:-1]
                if encabezado!='nombre,precio,cantidad':
                      raise ValueError('Encabezado erroneo!')
                if len(encabezado.split(',')) !=3:
                      raise ValueError('Encabezado no contiene 3 columnas')
                
                for dato in datos:
                    dato = dato.strip().lower()
                    valores = dato.split(',')
                    nombre = valores[0]
                    try:
                        precio = float(valores[1]) 
                        if precio < 0:
                              raise
                        cantidad = int(valores[2])
                        if cantidad < 0:
                              raise
                        inventario.append({'nombre':nombre,'precio':precio,'cantidad':cantidad})
                    except:
                        errores +=1
        
                print("Inventario cargado exitosamente")
                print(f"{errores} filas omitidas por datos erroneos")
                return inventario

        except ValueError as e:
              print(f"Error en la lectura del archivo: {e}")
        except FileNotFoundError as e:
            print(f"La ruta del archivo proporcionada no existe: {e}")
        except UnicodeDecodeError as e:
              print(f"El archivo contiene texto no apto para utf-8: {e}")

        