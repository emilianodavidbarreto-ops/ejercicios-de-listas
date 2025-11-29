print("--- CARRERA DE ATLETAS ---")
atletas = ["Ana", "Bruno", "Carlos", "Diana", "Elena"]
def adelantar_atleta(lista, nombre, posiciones):
    """Mueve a un atleta 'posiciones' más adelante (a un índice menor)."""
    try:
        idx_actual = lista.index(nombre)
        lista.pop(idx_actual)
        idx_nuevo = max(0, idx_actual - posiciones)
        lista.insert(idx_nuevo, nombre)
    except ValueError:
        print(f"Error: Atleta {nombre} no encontrado.")
adelantar_atleta(atletas, "Bruno", 2)
adelantar_atleta(atletas, "Diana", 1)
print("Orden final de llegada: ",atletas)