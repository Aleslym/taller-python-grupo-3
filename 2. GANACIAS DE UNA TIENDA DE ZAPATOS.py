def calcular_ganancias():
    total_compra = 0
    contador_compras = 0
    while True:
        entrada = input("Ingrese el valor de la compra realizada (presione 's' en minúscula para terminar): ")
        if entrada == 's':
            break

        try:
            valor_compra = float(entrada)
            total_compra += valor_compra
            contador_compras += 1
        except ValueError:
            print("Valor inválido. Por favor, ingrese un número válido o 's' para terminar.")

    ganancias = total_compra * 0.25
    return ganancias, contador_compras

ganancias_totales, cantidad_compras = calcular_ganancias()
print("Las ganancias totales son:", ganancias_totales)
print("Cantidad total de compras realizadas:", cantidad_compras)
        
    
    