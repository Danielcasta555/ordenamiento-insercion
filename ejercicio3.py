def ordenacion_insercion_caracteres(palabra):
    caracteres = list(palabra)
    
    for i in range(1, len(caracteres)):
        clave = caracteres[i]
        j = i - 1
        while j >= 0 and clave < caracteres[j]:
            caracteres[j + 1] = caracteres[j]
            j -= 1
        caracteres[j + 1] = clave
        
    palabra_ordenada = ''.join(caracteres)
    return palabra_ordenada

palabra = "colombia"
palabra_ordenada = ordenacion_insercion_caracteres(palabra)
print("Palabra ordenada alfabéticamente:", palabra_ordenada)
