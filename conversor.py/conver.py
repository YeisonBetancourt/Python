def divisas(tipo_pesos, valor_dolar, tienes):
        pesos = float(input("¿Cuantos " + tipo_pesos + " tienes?: "))
        dolares = pesos * valor_dolar 
        dolares = str(round(dolares, 4))
        print ("Tienes $" + dolares + " " + tienes) 
def elegido(moneda):
    print("Haz seleccionado " + moneda) 
    print("Asi que ahora elige, con que pais quieres cambiar tu moneda? 🤔")

menu = """Hola bienvenido a este grandioso conversor de monedas 🤑💱

¿Que moneda quieres cambiar? 🤔 

1- Peso Colombiano 
2- Peso Argentino 
3- Peso Mexicano
4- Dolar Americano  
5- Libra estarlina 
 
Elige una opcion (1, 2, 3, 4, 5) """

menu_seleccionar = int(input(menu))
if menu_seleccionar == 1:
    elegido("pesos Colombianos")
    colombia = """1- De pesos Colombianos a pesos Argentinos
    2- De pesos Colombianos a pesos Mexicanos 
    3- De pesos Colombianos a Dolares Americanos
    4- De pesos Colombinos a Libras Estarlinas
    
    Elige una opcion (1, 2, 3, ,4) """ 
    colombia_a = int(input(colombia))
    if colombia_a == 1:
        divisas("pesos Colmbianos", 0.024, "pesos Argentinos")
    elif colombia_a == 2:
        divisas("pesos Colombianos", 0.0053, "pesos Mexicanos")
    elif colombia_a == 3:
        divisas("pesos Colombianos", 0.00026, "Dolares Americanos")
    elif colombia_a == 4:
        divisas("pesos Colombianos", 0.00019, "Libras estarlinas")
    else:
        print ("Por favor, elige una opcion correcta💚")

elif menu_seleccionar == 2:
    elegido("pesos Argentinos")
    argentina = """1- De pesos Argentinos a pesos Colombianos
    2- De pesos Argentinos a pesos Mexicanos 
    3- De pesos Argentinos a Dolares Americanos
    4- De pesos Argentinos a Libras Estarlinas

    Elige una opcion (1, 2, 3, 4) """

    argentina_d = int(input(argentina))
    if argentina_d == 1:
        divisas("pesos Argentinos", 38.89, "pesos Colombianos")
    elif argentina_d == 2:  
        divisas("pesos Argentinos", 0.21, "pesos Mexicanos")
    elif argentina_d == 3:
        divisas("pesos Argentinos", 0.010, "Dolares Americanos")
    elif argentina_d == 4:
        divisas("pesos Argentinos", 0.00076, "Libras Estarlinas")
    else:
        print ("Por favor, elige una opcion correcta💚")
elif menu_seleccionar == 3:
    elegido("pesos Mexicanos")
    mexico = """1- De pesos Mexicanos a pesos Colombianos
    2- De pesos Mexicanos a pesos Argentinos
    3- De pesos Mexicanos a Dolares Americanos
    4- De pesos Mexicanos a Libras Estarlinas
    
    Elige una opcion (1, 2, 3, 4) """
    mexico_d = int(input(mexico))
    if mexico_d == 1:
        divisas("pesos Mexicanos", 186.98, "pesos Colombianos")
    elif mexico_d == 2:  
        divisas("pesos Mexicanos", 4.81, "pesos Argentinos")
    elif mexico_d == 3:
        divisas("pesos Mexicanos", 0.049, "Dolares Americanos")
    elif mexico_d == 4:
        divisas("pesos mexicanos", 0.0036, "Libras Estarlinas")
    else:
        print ("Por favor, elige una opcion correcta💚")
elif menu_seleccionar == 4:
    elegido("Dolares Americanos")
    america = """1- De Dolares Americanos a pesos Colombianos
    2- De Dolares Americanos a pesos Argentinos
    3- De Dolares Americanos a pesos Mexicanos
    4- De Dolares Mexicanos a Libras Estarlinas
    
    Elige una opcion (1, 2, 3, 4) """
    america_d = int(input(america))
    if america_d == 1:
        divisas("Dolares Americanos", 3836, "pesos Colombianos")
    elif america_d == 2:  
        divisas("Dolares Americanos", 98.61, "pesos Argentinos")
    elif america_d == 3:
        divisas("Dolares Americanos", 20.52, "pesos Mexicanos")
    elif america_d == 4:
        divisas("Dolares Americanos", 0.074, "Libras Estarlinas")
    else:
        print ("Por favor, elige una opcion correcta💚")
elif menu_seleccionar == 5:
    elegido("Libras Esyarlinas")
    reino_unido = """
    1- De Libras Estarlinas a pesos Colombianos
    2- De Libras Estarlinas a pesos Argentinos
    3- De Libras Estarlinas a Dolares Americanos
    4- De Libras Estarlinas a pesos Mexicanos
    
    Elige una opcion (1, 2, 3, 4) """
    reino_unido_d = int(input(reino_unido))
    if reino_unido_d == 1:
         divisas("Libras Estarlinas", 3836, "pesos Colombianos")
    elif reino_unido_d == 2:  
        divisas("Libras Estarlinas", 98.61, "pesos Argentinos")
    elif reino_unido_d == 3:    
        divisas("Libras Estarlinas", 20.52, "Dolares")
    elif reino_unido_d == 4:
        divisas("Libras Estarlinas", 0.074, "pesos Mexicanos")
    else:
        print ("Por favor, elige una opcion correcta💚")
else: 
    print("Por favor, elige una opcion correcta💚")




    
    
  








   
        

    














# def cambios(tipo_pesos, valor_dolar):
#     pesos = float(input("¿Cuantos pesos " +tipo_pesos+ " tienes?: "))  
#     dolares = pesos / valor_dolar 
#     dolares = str(round(dolares, 2  ))
#     print ("Tienes $" + dolares + " dolares Americanos")


# elige = """ Hola bienvenido al conversor de monedas, 

# 1 - Pesos Colombianos
# 2 - Pesos Argentinos
# 3 - Soles Peruanos
# 4 - Libras Estarlinas

# Por favor, elige una opcion: """

# opcion = int(input(elige)) 
# if  opcion == 1:
#     cambios("colombianos", 3.843)
# elif opcion == 2:
#     cambios("argentinos", 00.10)
# elif opcion == 3:
#     cambios("Soles Peruanos", 0.24)
# elif opcion == 4:
#     cambios("Libras Estarlinas", 1.37)
# else:
#     print ("Puto, pon un valor correcto")
