elige = """ Bienvenido al conversor de monedas 😀

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Soles Peruanos
4 - Libras Estarlinas

Por favor, elige una opcion: """

opcion = int(input(elige))
def cambios(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuantos pesos " +tipo_pesos+ " tienes?: "))  
    dolares = pesos / valor_dolar 
    dolares = str(round(dolares, 2  ))
    print ("Tienes $" + dolares + " dolares Americanos") 
if  opcion == 1:
    cambios("colombianos", 3.843)
elif opcion == 2:
    cambios("argentinos", 00.10)
elif opcion == 3:
    cambios("Soles Peruanos", 0.24)
elif opcion == 4:
    cambios("Libras Estarlinas", 1.37)
else:
    print ("Puto, pon un valor correcto")
