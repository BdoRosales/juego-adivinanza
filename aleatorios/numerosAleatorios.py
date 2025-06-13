import random

randomNumber = random.randint(0,15);

print ("JUEGO DE ADIVINANZA")
userNumber= int(input("Introduce un número del 0 al 15: "));

while userNumber<0 or userNumber>15:
    print("Número invalido, intenta otra vez")
    userNumber=int(input("Introduce un número válido: "))

while randomNumber!=userNumber:
    print("INTENTA DE NUEVO CON OTRO NÚMERO, TE DAMOS UNA PISTA")
    if randomNumber>userNumber:
        userNumber=int (input("Introduce un numero mas alto: "))
    elif randomNumber<userNumber:
        userNumber= int(input("Introduce un numero mas bajo: "))

print(f"GANASTE MI NÚMERO ERA: {randomNumber}")

