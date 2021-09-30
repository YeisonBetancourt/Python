def divisas(tipo_pesos, valor_dolar, tienes):
    pesos = float(input("¿Cuantos " + tipo_pesos + " tienes?: "))
    dolares = pesos * valor_dolar 
    dolares = str(round(dolares, 4))
    print ("Tienes $" + dolares + " " + tienes) 
def elegido(moneda, de_pesos, a_pesos1, a_pesos2, a_pesos3, a_pesos4):
    print("Haz seleccionado " + moneda) 
    print("Asi que ahora elige, con que pais quieres cambiar tu moneda? 🤔")
    print ("1- De " + de_pesos + " a " + a_pesos1)
    print ("2- De " + de_pesos + " a " + a_pesos2) 
    print ("3- De " + de_pesos + " a " + a_pesos3)                         
    print ("4- De " + de_pesos + " a " + a_pesos4)
                  
menu = """Hola bienvenido a este grandioso conversor de monedas 🤑💱

¿Que moneda quieres cambiar? 🤔 

1- Peso Colombiano 
2- Peso Argentino 
3- Peso Mexicano
4- Dolar Americano  
5- Libra Estarlina 
 
Elige una opcion (1, 2, 3, 4, 5) """

menu_seleccionar = int(input(menu))
if menu_seleccionar == 1:
    elegido("Pesos Colombianos", "Pesos Colombianos", "Pesos Argentinos", "pesos Mexicanos", "Dolares Americanos", "Libras Estarlinas")
    opcion_co = int(input("Elige una opcion (1, 2, 3, 4)"))  
    if opcion_co == 1:
        divisas("pesos Colombianos", 0.024, "Pesos Argentinos")
    elif opcion_co == 2:
        divisas("pesos Colombianos", 0.0053, "Pesos Mexicanos")
    elif opcion_co == 3:
        divisas("pesos Colombianos", 0.00026, "Dolares Americanos")
    elif opcion_co == 4:
        divisas("pesos Colombianos", 0.00019, "Libras Estarlinas")
    else:
        print ("Por favor, elige una opcion correcta💚")
elif menu_seleccionar == 2:
    elegido("Pesos Argentinos", "Pesos Argentinos", "Pesos Colombianos", "Pesos Mexicanos", "Dolares Americanos", "Libras Estarlinas")
    opcion_ar = int(input("Elige una opcion (1, 2, 3, 4)"))  
    if opcion_ar == 1:
        divisas("pesos Argentinos", 38.89, "Pesos Colombianos")
    elif opcion_ar == 2:  
        divisas("pesos Argentinos", 0.21, "Pesos Mexicanos")
    elif opcion_ar == 3:
        divisas("pesos Argentinos", 0.010, "Dolares Americanos")
    elif opcion_ar == 4:
        divisas("pesos Argentinos", 0.00076, "Libras Estarlinas")
    else:
        print ("Por favor, elige una opcion correcta💚")
elif menu_seleccionar == 3:
    elegido("Pesos Mexicanos", "Pesos Mexicanos", "Pesos Colombianos", "Pesos Argentinos", "Dolares Americanos", "Libras Estarlinas") 
    opcion_mx = int(input("Elige una opcion (1, 2, 3, 4)"))  
    if opcion_mx == 1:
        divisas("pesos Mexicanos", 186.98, "Pesos Colombianos")
    elif opcion_mx == 2:  
        divisas("pesos Mexicanos", 4.81, "Pesos Argentinos")
    elif opcion_mx == 3:
        divisas("pesos Mexicanos", 0.049, "Dolares Americanos")
    elif opcion_mx == 4:
        divisas("pesos Mexicanos", 0.0036, "Libras Estarlinas")
    else:
        print ("Por favor, elige una opcion correcta💚")
elif menu_seleccionar == 4:
    elegido("Dolares Americanos", "Dolares Americanos", "Pesos Colombianos", "Pesos Argentinos", "Pesos Mexicanos", "Libras Estarlinas")
    opcion_eu = int(input("Elige una opcion (1, 2, 3, 4)"))
    if opcion_eu == 1:
        divisas("Dolares Americanos", 3836, "Pesos Colombianos")
    elif opcion_eu == 2:  
        divisas("Dolares Americanos", 98.61, "Pesos Argentinos")
    elif opcion_eu == 3:
        divisas("Dolares Americanos", 20.52, "Pesos Mexicanos")
    elif opcion_eu == 4:
        divisas("Dolares Americanos", 0.074, "Libras Estarlinas")
    else:
        print ("Por favor, elige una opcion correcta💚")
elif menu_seleccionar == 5:
    elegido("Libras Estarlinas", "Libras Estralinas", "Pesos Colombianos", "Pesos Argentinos", "Dolares Americanos", "Pesos Mexicanos")
    opcion_ru = int(input("Elige una opcion (1, 2, 3, 4)"))
    if opcion_ru == 1:
         divisas("Libras Estarlinas", 3836, "Pesos Colombianos")
    elif opcion_ru == 2:  
        divisas("Libras Estarlinas", 98.61, "Pesos Argentinos")
    elif opcion_ru == 3:    
        divisas("Libras Estarlinas", 20.52, "Dolares")
    elif opcion_ru == 4:
        divisas("Libras Estarlinas", 0.074, "Pesos Mexicanos")
    else:
        print ("Por favor, elige una opcion correcta💚")
else: 
    print("Por favor, elige una opcion correcta💚")




    
    
  








   
        

    




# elegido("pesos Colombianos")
#     print ("1- De pesos Colombianos a pesos Argentinos")
#     print ("2- De pesos Colombianos a pesos Mexicanos") 
#     print ("3- De pesos Colombianos a Dolares Americanos")
#     print ("4- De pesos Colombinos a Libras Estarlinas")
#     opcion = int(input("""(Elige una opcion 1, 2, 3, 4)"""))  









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
