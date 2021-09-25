elige = """ Bienvenido al conversor de monedas 😀

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Soles Peruanos
4 - Libras Estarlinas

Por favor, elige una opcion: """

opcion = int(input(elige))

if  opcion == 1:
    pesos = float(input("¿Cuantos pesos Colombianos tienes?: "))
    valor_dolar = 3.834 
    dolares = pesos / valor_dolar 
    dolares = str(round(dolares, 1))
    print ("Tienes $" + dolares + " dolares Americanos")  

elif opcion == 2:
    pesos = float(input("¿Cuantos pesos Argentinos tienes?: "))
    valor_dolar = 0.010 
    dolares = pesos * valor_dolar 
    dolares = str(round(dolares, 1))
    print ("Tienes $" + dolares + " dolares Americanos")  

elif opcion == 3:
    pesos = float(input("¿Cuantos soles Peruanos tienes?: "))
    valor_dolar = 0.24 
    dolares = pesos * valor_dolar 
    dolares = str(round(dolares, 1))
    print ("Tienes $" + dolares + " dolares Americanos")  

elif opcion == 4:
    pesos = float(input("¿Cuantos libras estarlinas tienes?: "))
    valor_dolar = 1.37 
    dolares = pesos * valor_dolar 
    dolares = str(round(dolares, 1))
    print ("Tienes $" + dolares + " dolares Americanos") 

else:
    print ("Puto, pon un valor correcto")
