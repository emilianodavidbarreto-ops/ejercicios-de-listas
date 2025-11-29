print("--- RANKING DE JUGADORES ---")
puntajes = [450, 890, 320, 670, 1200, 550, 890]
puntajes.sort(reverse=True)
ranking_top3 = puntajes[:3]
print("Ranking completo (Mayor a Menor):", puntajes)
print(f"Oro: {ranking_top3[0]}")
print(f"Plata: {ranking_top3[1]}")
print(f"Bronce: {ranking_top3[2]}")