print("--- MAGO DE LAS LISTAS ---")
numeros_magicos = list(range(1, 11))
desaparecido_ultimo = numeros_magicos.pop()
desaparecido_primero = numeros_magicos.pop(0)
quedan = len(numeros_magicos)
desaparecidos = [desaparecido_primero, desaparecido_ultimo]
print("Números restantes:", numeros_magicos)
print(f"Cantidad de números que quedan: {quedan}")
print("Números que desaparecieron:",desaparecidos)