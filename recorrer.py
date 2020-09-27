def run():
    nombre = input("Dime tu nombre: ")
    nombre = nombre.split()

    for letra in nombre:
        print (letra.lower())

if __name__ == "__main__":
        run()
