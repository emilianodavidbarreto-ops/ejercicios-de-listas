print("--- ANÁLISIS DE VENTAS ---")
ventas = [1200, 1500, 980, 2100, 1800, 1650, 2300, 1900, 1750, 2000, 2200, 2500]
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
venta_max = max(ventas)
posicion_idx = ventas.index(venta_max)
mes_max = meses[posicion_idx]
posicion_anual = posicion_idx + 1
promedio_ventas = sum(ventas) / len(ventas)
print(f"Ventas más altas: {venta_max}")
print(f"Mes con ventas más altas: {mes_max}")
print(f"Posición en el año: {posicion_anual}")
print(f"Promedio de ventas anual: {promedio_ventas:.2f}")