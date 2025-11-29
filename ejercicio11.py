print("--- LIMPIEZA DE LISTA ---")
lista_sucia = [1, 2, None, 3, 2, 4, None, 1, 5, 3]
sin_nulos = [x for x in lista_sucia if x is not None]
lista_limpia = list(set(sin_nulos))
lista_limpia.sort()
print("Lista original:", lista_sucia)
print("Lista limpia (sin nulos ni duplicados): ",lista_limpia)