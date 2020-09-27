def comprobacion(numero):
    if (numero == 1):
        return False
    else:
        contador = 0
        for i in range(2, numero - 1):
            if numero % i == 0:
                contador += 1

    if contador == 0:
        return True
    else:
        return False


def main():
    numero= int(input("Dime un numero: "))


    if (comprobacion(numero)):
        print("Es primo")
    else:
        print("No es primo")


if __name__ == "__main__":
    main()