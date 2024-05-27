print ("Algoritmo para caracterizar un año si es o no bisiesto")

año = int(input("Ingrese un año: "))
caracterizacion= año % 4


if caracterizacion ==0:
    print(año,",es un año bisiesto.")
else:
    print(año,",no es un año bisiesto.")