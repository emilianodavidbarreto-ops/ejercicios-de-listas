print("--- PIZZERÍA ---")
ing = ["queso", "tomate", "anchoas", "jamón"]
ing.append("peperoni")
ing.append("pezcado")
ing.append("cebolla")
if "anchoas" in ing:
    ing.remove("anchoas")
print("Ingredientes finales:",ing)