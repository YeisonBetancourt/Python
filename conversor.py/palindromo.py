def palindromo(palabra): 
    palabra = palabra.replace(' ', ' ')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
         return True
    else:
         return False     
         
def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:   
        print('Es palindromo')
    else:
        print('No es palindromo')

if __name__ == '__main__':
    run()


    
# def pantalla():
#     print("""Este es el proceso
#     r1 = 690 
#     r2 = 23
#     r3 = 67
#     r4 = 10
#     rt = (r1 + r2 + r3 + r4)
#     vt = 40
#     it = (vt / rt)
#     vr1 = (r1 * it)
#     vr2 = (r2 * it)
#     vr3 = (r3 * it)
#     vr4 = (r4 * it)
#     vt = (vr1 + vr2 + vr3 + vr4)
#     vt = str(vt) """)
