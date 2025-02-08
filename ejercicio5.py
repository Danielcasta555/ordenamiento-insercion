def ordenacion_insercion_distancias(distancias):
    for i in range(1, len(distancias)):
        clave = distancias[i]
        j = i - 1
        while j >= 0 and clave < distancias[j]:
            distancias[j + 1] = distancias[j]
            j -= 1
        distancias[j + 1] = clave
    return distancias

distancias_entre_ciudades = [120, 75, 300, 200, 50, 150]
distancias_ordenadas = ordenacion_insercion_distancias(distancias_entre_ciudades)
print("Distancias ordenadas:", distancias_ordenadas)

