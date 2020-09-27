<<<<<<< HEAD
def main():

    numero_elegido = int(input("Dime un numero: "))
    prueba = 0

    while prueba**2 < numero_elegido:
        prueba += 1

    if prueba**2 == numero_elegido:
        print(f"La raiz cuadradada de {numero_elegido} es {prueba}")
    else:
        print(f"{numero_elegido} no tiene raiz cuadrada")

if __name__ == "__main__":
=======
def main():

    numero_elegido = int(input("Dime un numero: "))
    prueba = 0

    while prueba**2 < numero_elegido:
        prueba += 1

    if prueba**2 == numero_elegido:
        print(f"La raiz cuadradada de {numero_elegido} es {prueba}")
    else:
        print(f"{numero_elegido} no tiene raiz cuadrada")

if __name__ == "__main__":
>>>>>>> f43663b2288914b75589a4912e4d67cd0413a239
    main()