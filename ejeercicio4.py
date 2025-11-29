print("--- INVERSIÓN TEMPORAL ---")
eventos = ["Nacimiento", "Escuela", "Universidad", "Trabajo", "Jubilación"]
eventos_reciente_antiguo = eventos[:]
eventos_reciente_antiguo.reverse()
#crea una copia alternativa 
linea_alternativa = eventos_reciente_antiguo.copy()
print("Eventos (Reciente a Antiguo):", eventos_reciente_antiguo)
print("Copia para Línea Alternativa:", linea_alternativa)