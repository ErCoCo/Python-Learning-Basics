<<<<<<< HEAD
menu = """
Bienvenido al conversor de monedas 💰💸

1- pesos colombianos
2- pesos argentinos
3- pesos mexicanos

elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + 'dolares') 

elif opcion == 2:
    pesos = input("cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + 'dolares') 

elif opcion == 3:
    pesos = input("cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + 'dolares') 

else:
    print ("Eso no puedo hacerlo 🤯")
=======
menu = """
Bienvenido al conversor de monedas 💰💸

1- pesos colombianos
2- pesos argentinos
3- pesos mexicanos

elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + 'dolares') 

elif opcion == 2:
    pesos = input("cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + 'dolares') 

elif opcion == 3:
    pesos = input("cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + 'dolares') 

else:
    print ("Eso no puedo hacerlo 🤯")
>>>>>>> f43663b2288914b75589a4912e4d67cd0413a239
