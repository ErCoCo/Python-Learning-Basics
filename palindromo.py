<<<<<<< HEAD
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra = input('Dime una palabra: ')
    comprobacion = palindromo(palabra)

    if comprobacion == True:
        print("Es palindromo")
    else:
        print('No es palindromo')


if __name__ == '__main__':
=======
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra = input('Dime una palabra: ')
    comprobacion = palindromo(palabra)

    if comprobacion == True:
        print("Es palindromo")
    else:
        print('No es palindromo')


if __name__ == '__main__':
>>>>>>> f43663b2288914b75589a4912e4d67cd0413a239
    main()