print("--- PALETA DE COLORES ---")
def paleta_colores(colores):
    """
    Modifica la lista de colores, agrega elementos, y retorna la original 
    modificada y la invertida.
    """
    colores.insert(0, "blanco")
    colores.append("negro")
    paleta_invertida = colores[::-1]
    
    return colores, paleta_invertida
colores = ["rojo", "verde", "azul", "amarillo"]
paleta_modificada, paleta_invertida = paleta_colores(colores)
print("Paleta modificada:", paleta_modificada)
print("Paleta invertida:", paleta_invertida)