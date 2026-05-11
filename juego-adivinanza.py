import random

# ======== VARIABLES ========
numero_secreto = random.randint(1,100)
adivinado = False
intentos = 0
intentos_maximos = 10

# ======== INTRODUCCIÓN ========

print("Hola! Adiviná en qué número estoy pensando del 1 al 100!")

# ======== JUEGO ========

while not adivinado and intentos < intentos_maximos:
    try:
        entrada = input("Introduce un número entre 1 y 100: ")
        numero = int(entrada)

        # Validar que el número esté dentro del rango estipulado
        if numero < 1 or numero > 100:
             print("❌ Introduce un número entre 1 y 100.")
             continue
        
        intentos += 1

        if numero == numero_secreto:
            print(f"⭐ ¡Adivinaste el número en {intentos} intentos!")
            adivinado = True

        elif numero < numero_secreto:
             print("⏫ El número es mayor al ingresado.")
        else:
             print("⏬ El número es menor al ingresado.")
    
    except ValueError:
            print("❌ Por favor, introduce un número válido.")
            continue

# ======== RESULTADO ========

if not adivinado:
     print(f"Perdiste! El número era {numero_secreto}.")
     
print(f"Gracias por jugar! Usaste {intentos} de {intentos_maximos} intentos.")
