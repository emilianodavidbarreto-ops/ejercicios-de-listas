print("--- JUEGO DE BATALLA POR TURNOS ---")
import random

equipo_a = ["Guerrero", "Mago", "Arquero"]
equipo_b = ["Orco", "Goblin", "Troll"]
vida_personajes = {p: 100 for p in equipo_a + equipo_b}

def atacar(atacante, defensor):
    """Simula un ataque con daño aleatorio (20-50 puntos)."""
    dano = random.randint(20, 50)
    vida_personajes[defensor] -= dano
    print(f"  {atacante} ataca a {defensor} con {dano} de daño.")
    print(f"  Vida restante de {defensor}: {vida_personajes[defensor]} HP.")
    return vida_personajes[defensor] <= 0

def turno_batalla(equipo_atacante, equipo_defensor):
    """Ejecuta un turno de batalla para el equipo atacante."""
    if not equipo_atacante:
        return equipo_defensor

    atacante = equipo_atacante.pop(0) 
    

    defensor = equipo_defensor[0]

    muerto = atacar(atacante, defensor)
    
    if muerto:
        equipo_defensor.pop(0)
        print(f"  💀 ¡{defensor} ha sido eliminado!")
    else:
        equipo_atacante.append(atacante)
        
    return equipo_defensor

turno = 0
while equipo_a and equipo_b:
    turno += 1
    print(f"\n===== TURNO {turno} =====")
    
    # 1. Turno de Equipo A
    if equipo_a and equipo_b:
        print("-> Turno de Equipo A:")
        equipo_b = turno_batalla(equipo_a, equipo_b)

    # 2. Turno de Equipo B
    if equipo_b and equipo_a:
        print("-> Turno de Equipo B:")
        equipo_a = turno_batalla(equipo_b, equipo_a)

# Determina el ganador
if equipo_a:
    print("\n🏆 ¡El Equipo A ha ganado la batalla!")
    print("Supervivientes del Equipo A:", equipo_a)
elif equipo_b:
    print("\n🏆 ¡El Equipo B ha ganado la batalla!")
    print("Supervivientes del Equipo B:", equipo_b)
else:
    print("\n¡Es un empate! Ambos equipos fueron eliminados.")