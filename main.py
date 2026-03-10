def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    producto.append(producto)

    agregar_producto()

