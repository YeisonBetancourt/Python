# def palindromo(palabra): 
#     palabra = palabra.replace(' ', '')
#     palabra = palabra.lower()       
#     palabra_invertida = palabra[::-1]
#     if palabra == palabra_invertida:
#          return True
#     else:
#          return False     
         
# def run():
#     palabra = input('Escribe una palabra: ')
#     es_palindromo = palindromo(palabra)
#     if es_palindromo == True:   
#         print('Es palindromo')


#     else:
#         print('No es palindromo')

# if __name__ == '__main__':
#     run()



def si(palabra):

    palabra = palabra.lower()
    if palabra == "si":
        return True
    else:
        return False
def run(): 
    print("Diga si para continuar")
    palabra = input("Desea continuar con el programa? ")
    es_si = si(palabra)
    while (es_si == True):
        print("Diga si para continuar")
        palabra = input("Desea continuar con el programa? ")
        

    else:
        print("Hasta la vista")  
if __name__ == '__main__':  
    run()  

