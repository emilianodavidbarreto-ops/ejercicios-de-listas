print("--- MALABARISTA DE NÚMEROS ---")
def malabares(numeros):
    """Toma el último elemento y lo pone al inicio, repite 3 veces."""
    for _ in range(3):
        ultimo = numeros.pop()
        numeros.insert(0, ultimo)
    return numeros
print(malabares([1, 2, 3, 4, 5]))
# Resultado esperado: [3, 4, 5, 1, 2]