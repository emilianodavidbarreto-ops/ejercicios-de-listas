print("--- MÁQUINA TRAGAMONEDAS ---")
import random
simbolos_posibles = ["🍒", "🍋", "🔔", "💎", "⿧"]

def maquina_tragamonedas(simbolos):
    """Genera 3 símbolos aleatorios y determina el premio."""
    resultado = random.choices(simbolos, k=3)
    num_simbolos_unicos = len(set(resultado))
    
    premio = ""
    if num_simbolos_unicos == 1:
        premio = "Jackpot 💰"
    elif num_simbolos_unicos == 2:
        premio = "Premio menor 🎁"
    else:
        premio = "Sin premio 😢"    
    return resultado, premio
for _ in range(3):
    simbolos_generados, resultado_premio = maquina_tragamonedas(simbolos_posibles)
    print(f"Resultado: {simbolos_generados} -> {resultado_premio}")