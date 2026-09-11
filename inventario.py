print("Proyecto Inventario Avance 3")
print ()

producto = "Computadora"
precio = 15000
cantidad = 10
stock_minimo = 3

producto2 = "Telefono"
precio2 = 8000
cantidad2 = 10
stock_minimo2 = 3

producto3 = "Raton"
precio3 = 800
cantidad3 = 10
stock_minimo3 = 3

def comproducto(producto, precio, cantidad, stock_minimo):

    comprado = 0

    while cantidad > 0:
        print("Producto: ", producto)
        print("Precio: ", precio)
        print("Cantidad disponible: ", cantidad)

        total = precio * cantidad

        print("Total inventario: ", total)

        venta = int(input("------ Cuantos compras?: "))

        if venta > cantidad:
            print("------ No hay suficientes unidades ------")
        else:
            cantidad = cantidad - venta
            comprado = comprado + venta
            print("------ Unidades restantes: ", cantidad)
            if cantidad == 0:
                print("------ Ya no hay ;( ------")
            elif cantidad <= stock_minimo:
                print("------ Quedan pocos ------")
            if cantidad > 0:
                continuar = input("Quieres seguir comprando? (si o no): ")
                if continuar == "no":
                    break
                elif continuar == "si":
                    print("------ ok ------")
                else:
                    print("------ Eso es un no ------")
                    break

    return cantidad, comprado

cantidad, comprado = comproducto(producto, precio, cantidad, stock_minimo)
cantidad2, comprado2 = comproducto(producto2, precio2, cantidad2, stock_minimo2)
cantidad3, comprado3 = comproducto(producto3, precio3, cantidad3, stock_minimo3)

print()
print("========== COMPRA ==========")
print("Computadoras: ", comprado)
print("Telefonos: ", comprado2)
print("Ratones: ", comprado3)
