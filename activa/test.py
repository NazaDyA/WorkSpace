from fuzzywuzzy import fuzz

def comparar_cadenas_laxas(cadena1, cadena2):
    # Convertir ambas cadenas a minúsculas y eliminar espacios en blanco adicionales
    cadena1 = cadena1.lower().strip()
    cadena2 = cadena2.lower().strip()

    # Calcular la similitud entre las cadenas utilizando el coeficiente de similitud difusa
    similitud = fuzz.ratio(cadena1, cadena2)
    print(similitud)
    # Determinar si la similitud es alta para considerarlas como emparejadas
    if similitud >= 80:  # Puedes ajustar este umbral según tus necesidades
        
        return True
    else:
        return False

# Casos de prueba
cadena1 = "Av. Donato Alvarez 7980"
cadena2 = "TTE GRAL DONATO ALVAREZ 7954"

resultado = comparar_cadenas_laxas(cadena1, cadena2)
print(resultado)


cadena1 = "Av. Donato Alvarez 7980"
cadena2 = " SAN MARTIN 512"

resultado = comparar_cadenas_laxas(cadena1, cadena2)
print(resultado)