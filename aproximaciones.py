def main():

    #variables de entrada y salida
    numero_elegido = int(input("Dime un numero: "))
    respuesta = 0.0

    #variables de aproximacion
    epsilon = 0.001                 #cuanto nos queremos aproximar
    aproximacion = epsilon**2      #cuanto nos vamos acercando

    while abs(respuesta**2 - numero_elegido) >= epsilon and respuesta <= numero_elegido:
        print(abs(respuesta))
        respuesta += aproximacion

    if abs(respuesta**2 - numero_elegido) >= epsilon:
        print(f"{numero_elegido} no tiene raiz cuadrada")
    else:
        print(f"la raiz cuadrada de {numero_elegido} es {respuesta}")

if __name__ == "__main__":
    main()