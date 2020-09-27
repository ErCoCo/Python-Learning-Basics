import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un numero del 1 al 100: "))
        
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            numero_elegido = int(input("Te quedaste corto, prueba otra vez: "))
        elif numero_elegido > numero_aleatorio:
            numero_elegido = int(input("Te pasaste, prueba otra vez: "))
        else:
            numero_elegido = int(input("No reconozco ese numero, escribe un numero del 1 al 100"))
    print("El numero era " + str(numero_aleatorio) + ", Ganaste!")

if __name__ == '__main__':
    run()