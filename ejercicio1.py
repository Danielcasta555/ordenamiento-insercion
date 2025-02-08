def ordenacion_insercion(edades):
    for i in range(1, len(edades)):
        clave = edades[i]
        j = i - 1
        while j >= 0 and clave < edades[j]:
            edades[j + 1] = edades[j]
            j -= 1
            edades[j + i] = clave 
    return edades

edades = [34, 23, 42, 19, 56, 31]
edades_ordenadas = ordenacion_insercion(edades)
print("edades ordenadas:", edades_ordenadas)
