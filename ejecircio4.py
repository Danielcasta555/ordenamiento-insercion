def ordenacion_insercion_ventas(ventas):
    for i in range(1, len(ventas)):
        clave = ventas[i]
        j = i - 1
        while j >= 0 and clave < ventas[j]:
            ventas[j + 1] = ventas[j]
            j -= 1
        ventas[j + 1] = clave
    return ventas

ventas_diarias = [150, 320, 210, 180, 275, 400]
ventas_ordenadas = ordenacion_insercion_ventas(ventas_diarias)
print("ventas diarias ordenadas:", ventas_ordenadas)    