def ordenacion_insercion_descedente(puntuacion):
    for i in range(1, len(puntuacion)):
        clave = puntuacion[i]
        j = i - 1
        while j >= 0 and clave > puntuacion[j]:
            puntuacion[j + 1] = puntuacion[j]
            j -= 1
            puntuacion[j + 1] = clave
    return puntuacion

puntuacion = [250, 300, 150, 450, 200, 400]
puntuacion_ordenadas = ordenacion_insercion_descedente(puntuacion)
print("Puntuacion Ordenadas", puntuacion_ordenadas) 