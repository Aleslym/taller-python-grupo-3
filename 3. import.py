print("juego_adivinanza ") 
numero_secreto=3
intentos =1
int (input("Adivina un numero entre 1 y 5 ingresa su intento: " ))
numero = int(input("adivina un numero que se encuentre entre 1 a 5 aleatorio ingrese su intento: ")) 

if numero ==3:
    print(f"Felicidades adivinaste el numero.")

else:
    print("El numero no se encuentra,intentalo de nuevo, el numero es:  " ,numero_secreto)
