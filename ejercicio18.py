print("--- DJ AUTOMÁTICO ---")
cola_reproduccion = []

def agregar_album(canciones):
    """Agrega álbumes completos (múltiples canciones) al final de la cola."""
    cola_reproduccion.extend(canciones)

def reproducir_siguiente():
    """Reproduce la siguiente canción (se elimina de la cola)."""
    if cola_reproduccion:
        return cola_reproduccion.pop(0)
    return "Cola vacía."

def agregar_urgente(cancion):
    """Agrega canciones urgentes que suenen inmediatamente (al inicio de la cola)."""
    cola_reproduccion.insert(0, cancion)

def mostrar_proximas():
    """Muestra las próximas 3 canciones en cola."""
    return cola_reproduccion[:3]
agregar_album(["A1", "A2", "A3"])
agregar_album(["B1", "B2"])
print("Próximas 3 en cola:", mostrar_proximas())

print("Reproduciendo:", reproducir_siguiente())
agregar_urgente("Urgente DJ Set")
print("Agregada urgente. Próximas 3:", mostrar_proximas())

print("Reproduciendo:", reproducir_siguiente())
print("Próximas 3 en cola:", mostrar_proximas())