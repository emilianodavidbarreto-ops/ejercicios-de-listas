print("--- CINE NOSTÁLGICO ---")
peliculas = [
    ("Matrix", 1999),
    ("Inception", 2010),
    ("Titanic", 1997),
    ("Avatar", 2009)
]

peliculas_ordenadas = sorted(peliculas, key=lambda peli: peli[1])
print("Películas ordenadas:", peliculas_ordenadas)
vistas = []
for _ in range(3):
    if peliculas_ordenadas:
        vistas.append(peliculas_ordenadas.pop(0))
print("Películas vistas (las 3 más antiguas):", vistas)
print("Películas restantes:", peliculas_ordenadas)