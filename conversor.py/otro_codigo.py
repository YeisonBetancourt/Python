# def calculos(multiplo, resultado_multiplicacion):
#     calculo = False
#     for multiplicador in range(11):# se busca el resultado en todos los resultados
#         multiplicacion = multiplo * multiplicador
#         if resultado_multiplicacion == multiplicacion:
#             break
#         calculo = True    
#     return calculo

# def operacion(numero_selector):
#     multiplo = int(numero_selector)
#     for multiplicador in range(11):#muestra la tabla de multiplicar que seleciona el usuario
#         print(f'{multiplo} x {multiplicador} = ')

#     resultado_multiplicacion = int(input('escribe el resultado de cualquier multiplicacion'))

#     respuesta = calculos(multiplo, resultado_multiplicacion)
#     if respuesta == True:
#         print('respuesta correcta')
#     else:
#         print('respuesta incorrecta')

# def run():
#     decision = 'si'
#     while decision == 'si':#busca que las opciones y el programa se reproduzca las veces que desee el usuario
#         print('bienvenido aprende las tablas de multiplicar')
#         print('''selecciona la tabla que deseas practicar
# [1] para tabla del 1
# [2] para tabla del 2
# [3] para tabla del 3
# [4] para tabla del 4
# [5] para tabla del 5
# [6] para tabla del 6
# [7] para tabla del 7
# [8] para tabla del 8
# [9] para tabla del 9
# [10] para tabla del 10
# ''')
#         numero_selector = input('escribe la selección aca: ')
#         ejecucion_de_operacion = operacion(numero_selector)
#         decision = input('si deseas continuar escribe SI o NO para salir ')
#         decision = decision.lower()# vuelve todas las respuestas a minusculas  


# if __name__ == '__main__':
#     run()







# def saludo():
#     print("""BIENVENIDO A LAS TABLAS""")

# def tabla_del_numero():
    
#     limite = int(input("¿Hasta que número?\n"))
#     contador = 0

#     while contador <= limite:
#         resultado = numero * contador
#         print(f"{numero} * {contador} = {resultado}")
#         contador += 1

# def pedirNumeroEntero():
 
#     correcto=False
#     num=0
#     while(not correcto):
#         try:
#             numero = int(input("¿Que tabla deseas calcular?\n"))
#             correcto=True
#         except ValueError:
#             print('Error, introduce un numero entero')
     
#     return numero
 


# if __name__ == "__main__":
#     saludo()
#     numero = pedirNumeroEntero()
#     tabla_del_numero()



def run():
    mensaje="Bienvenido al juego de ADIVINA LA LETRA, tienes 10 intentos, BUENA SUERTE AMIGO(A) 😊😈😊"
    print(mensaje)
    contador=1 #comenzamos desde 1
    limite=11 #Hasta el 10
    while contador<limite:
        letra=input("Adivina la letra: ")
        if ((letra!='h') and (letra!='H')): #Comprobamos si es la letra gandora
            print("No es esa letra, ya vas ", contador,"intentos de 10")
            #damos a conocer los intentos
            if contador==10: #Mensaje cuando llegues al límite
                print("YA PERDISTE!! AJAJAJA 😈🤡😂")
        else: #En el caso de ser la letra ganadora
            print("Esa es la letra, GANASTE, pense que no lo lograrías 😒👿😛")
            break
        contador += 1


if __name__=="__main__":
    run()




# for i in range(6):
#     if i == 5:
#         print("Figaroooo")
#         break
#     print("Galileo")