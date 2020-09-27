<<<<<<< HEAD
def conversor(moneda, valor_dolar):
    pesos = input("cuantos " +  moneda  + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + ' dolares') 


menu = """
Bienvenido al conversor de monedas 💰💸

1- pesos colombianos
2- pesos argentinos
3- pesos mexicanos

elige una opcion: """


opcion = int(input(menu))

if opcion == 1:
    conversor("pesos colombianos", 3875)

elif opcion == 2:
    conversor("pesos argentinos", 65)

elif opcion == 3:
    conversor("pesos colombianos", 24 )

else:
    print ("Eso no puedo hacerlo 🤯")

=======
def conversor(moneda, valor_dolar):
    pesos = input("cuantos " +  moneda  + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('tienes $' + dolares + ' dolares') 


menu = """
Bienvenido al conversor de monedas 💰💸

1- pesos colombianos
2- pesos argentinos
3- pesos mexicanos

elige una opcion: """


opcion = int(input(menu))

if opcion == 1:
    conversor("pesos colombianos", 3875)

elif opcion == 2:
    conversor("pesos argentinos", 65)

elif opcion == 3:
    conversor("pesos colombianos", 24 )

else:
    print ("Eso no puedo hacerlo 🤯")

>>>>>>> f43663b2288914b75589a4912e4d67cd0413a239
    