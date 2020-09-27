<<<<<<< HEAD
def main():
    nombre1 = input("Cual ese el primer usuario: ")
    nombre2 = input("Cual es el segundo nombre: ")
    edad1 = int(input("Cual es la edad del primer usuario: "))
    edad2 = int(input("Cual es la edad del segundo usuario: "))

    if edad1 > edad2:
        print(f'{nombre1} es mayor que {nombre2}')
    elif edad2 > edad1:
        print(f'{nombre2} es mayor que {nombre1}')
    else:
        print(f'{nombre1} y {nombre2} tienen la mismas edad')

if __name__ == "__main__":
=======
def main():
    nombre1 = input("Cual ese el primer usuario: ")
    nombre2 = input("Cual es el segundo nombre: ")
    edad1 = int(input("Cual es la edad del primer usuario: "))
    edad2 = int(input("Cual es la edad del segundo usuario: "))

    if edad1 > edad2:
        print(f'{nombre1} es mayor que {nombre2}')
    elif edad2 > edad1:
        print(f'{nombre2} es mayor que {nombre1}')
    else:
        print(f'{nombre1} y {nombre2} tienen la mismas edad')

if __name__ == "__main__":
>>>>>>> f43663b2288914b75589a4912e4d67cd0413a239
    main()