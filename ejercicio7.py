print("--- FUSIÓN DE MENÚS ---")
menu_a = ["hamburguesa", "pizza", "ensalada", "sopa"]
menu_b = ["pizza", "pasta", "ensalada", "tacos"]
menu_combinado = menu_a + menu_b
menu_sin_duplicados = list(set(menu_combinado))
print("Menú fusionado sin duplicados:", menu_sin_duplicados)