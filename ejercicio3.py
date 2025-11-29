print("--- CONTADOR DE PUNTOS ---")
puntuaciones = [50, 100, 75, 100, 90, 100, 85, 100]
puntuacion_querida = 100
conteo = puntuaciones.count(puntuacion_querida)
try:
    primera_ronda = puntuaciones.index(puntuacion_querida) + 1
except ValueError:
    primera_ronda = "No se encontró"
print(f"Puntuación {puntuacion_querida} obtenida {conteo} veces.")
print(f"Primera vez en la ronda: {primera_ronda}")