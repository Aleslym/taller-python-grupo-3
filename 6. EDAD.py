nombre = input("por favor ingrese su nombre: ")
edad = int (input("ahora ingrese su EDA: "))

if edad > 18:
    print (f"Hola,{nombre} eres una persona mayor de edad y puedes votar.")
else:
    print (f"Hola,{nombre} eres una persona menor de edad y no  puedes votar.")