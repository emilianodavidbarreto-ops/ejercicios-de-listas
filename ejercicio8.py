print("--- BIBLIOTECA PERSONAL ---")
libros = [
    {"titulo": "El Hobbit", "paginas": 310},
    {"titulo": "1984", "paginas": 328},
    {"titulo": "El Principito", "paginas": 96}
]
libros_ordenados = sorted(libros, key=lambda libro: libro["paginas"])
print("Libros ordenados por páginas:")
for libro in libros_ordenados:
    print(f"- {libro['titulo']}: {libro['paginas']} páginas")