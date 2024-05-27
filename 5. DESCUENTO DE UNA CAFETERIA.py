try:
    consumo_total = float(input("Ingrese el total del consumo en la cafetería: $"))
    descuento = 0
    
    if consumo_total >=100000:
        descuento =5
    if consumo_total >=300000:
        descuento =10

    
    pago_total_sin_descuento = consumo_total
    descuento_compra =(consumo_total*descuento)/100
    pago_total_con_descuento =(consumo_total-descuento_compra)
    
    print("Pago total sin descuento: $ ",pago_total_sin_descuento)
    print("Pago total con descuento: $ ",pago_total_con_descuento)
    
except ValueError:
    print("Error: Por favor ingrese un valor numérico válido.")