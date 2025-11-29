print("--- JUEGO DE DADOS ---")

import random
lanzamientos = [random.randint(1, 6) for _ in range(20)]
conteo_resultados = {}
for numero in lanzamientos:
    conteo_resultados[numero] = conteo_resultados.get(numero, 0) + 1
resultados_finales = {i: conteo_resultados.get(i, 0) for i in range(1, 7)}
print("Lanzamientos:", lanzamientos)
print("Conteo de cada número:")
for num, veces in sorted(resultados_finales.items()):
    print(f"  {num}: {veces} veces")