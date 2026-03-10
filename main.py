def agregar_producto(productos):
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    producto.append(productos)

def mostrar_producto(productos):
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")  

def actualizar_producto(productos):
    nombre = input("Ingrese el nombre del producto a actualizar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad
            print("Producto actualizado exitosamente.")
            return
    print("Producto no encontrado.")

    def eliminar_producto(productos):
        nombre = input("Ingrese el nombre del producto a eliminar: ")
        for producto in productos:
            if producto["nombre"] == nombre:
                productos.remove(producto)
                print("Producto eliminado exitosamente.")
                return
        print("Producto no encontrado.")
