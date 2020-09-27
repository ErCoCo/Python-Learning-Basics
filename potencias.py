def run():
    LIMITE = 1000

    contador = 0
    potencia = 1

    # while potencia < LIMITE:
    #     print("2 elevado a " + str(contador) + " es igual a: " + str(potencia))
    #     contador = contador + 1
    #     potencia = 2**contador


    for contador in range(12):
    print("2 elevado a " + str(contador) + " es igual a: " + str(potencia))
    potencia = 2**contador

if __name__ == "__main__":
    run()