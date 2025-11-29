carrito = []
precios = {"manzana": 2, "pan": 1.5, "leche": 3, "huevos": 4}

def agregar_producto(producto):
    """Agrega productos al carrito."""
    carrito.append(producto)

def calcular_cantidad():
    """Calcula la cantidad de cada producto."""
    conteo = {}
    for producto in carrito:
        conteo[producto] = conteo.get(producto, 0) + 1
    return conteo

def eliminar_producto(producto):
    """Elimina productos específicos uno a uno."""
    if producto in carrito:
        carrito.remove(producto)
        return f"Eliminado 1 {producto}."
    return f"{producto} no está en el carrito."

def calcular_total_compra():
    """Calcula el total de la compra agrupando por producto."""
    total = 0
    conteo = calcular_cantidad()
    for producto, cantidad in conteo.items():
        if producto in precios:
            total += precios[producto] * cantidad
        else:
            print(f"Advertencia: Precio de {producto} no encontrado.")
    return total

# Demostración
agregar_producto("manzana")
agregar_producto("leche")
agregar_producto("manzana")
agregar_producto("pan")

print("\n--- 🏪 SUPERMERCADO INTELIGENTE ---")
print("Carrito:", carrito)
print("Cantidad por producto:", calcular_cantidad())
print(eliminar_producto("manzana"))
print("Total de la compra:", calcular_total_compra())