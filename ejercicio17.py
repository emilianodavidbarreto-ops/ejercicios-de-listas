print("--- INVENTARIO DE JUEGO RPG ---")
inventario = []
def recoger_objeto(objeto):
    """Recoge un objeto y lo agrega al inventario."""
    inventario.append(objeto)

def verificar_objeto(objeto):
    """Verifica si tienes un objeto específico y cuántos."""
    conteo = inventario.count(objeto)
    return conteo

def usar_objeto(objeto):
    """Usa/vende un objeto (elimina uno a la vez)."""
    if objeto in inventario:
        inventario.remove(objeto)
        return f"Usaste/Vendiste un(a) {objeto}."
    else:
        return f"No tienes {objeto} en el inventario."

def organizar_inventario():
    """Organiza el inventario alfabéticamente."""
    inventario.sort()

# Demostración
recoger_objeto("Espada")
recoger_objeto("Poción de vida")
recoger_objeto("Escudo")
recoger_objeto("Poción de vida")

print("Inventario inicial:", inventario)

print(f"Tienes pociones de vida: {verificar_objeto('Poción de vida')}")

print(usar_objeto("Poción de vida"))
print(usar_objeto("Llave"))

organizar_inventario()
print("Inventario organizado:",inventario)