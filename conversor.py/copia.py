def nombre_tabla(welcome, tablita):
    welcome = welcome.lower()
    welcome = welcome.replace(" ", "")
    if welcome == tablita:
        return True
    else:
        return False
        
def resolviendo (numero, rango):
    for contador in range (numero, rango):
        print(contador*1)

def operacion (operador):
    print("Sobre que tabla de " + operador + " quieres actuar🤔:  ")
    for contador in range (1, 10):
        print (str(contador) + "- " + "tabla del " + str(contador))
    numero_elegido = int(input("Elige una tabla de " + operador + ": "))
    if numero_elegido == 1:
        resolviendo(0, 10)
    elif numero_elegido == 2:
        resolviendo(1, 11)
    elif numero_elegido == 3:
        resolviendo(2, 12)    
    elif numero_elegido == 4:
        resolviendo(3, 13)
    elif numero_elegido == 5:
        resolviendo(4, 14)
    elif numero_elegido == 6:
        resolviendo(5, 15)
    elif numero_elegido == 7:
        resolviendo(6, 16)
    elif numero_elegido == 8:
        resolviendo(7, 17)
    elif numero_elegido == 9:
        resolviendo(8, 18)
    else:
        print("Elija una opcion correcta 💚")                  


def run():
    welcome = input("""Hola👋, bienvenido a este increible programa donde podras saber:
    
    1- Tabla de adicion
    2- Tabla de sutracion
    3- Tabla de multiplicacion
    4- Tabla de la division 
    
    ¿Que tabla necesitas usar? (EJEMPlO: Tabla de adicion) """)
    es_tabla = nombre_tabla(welcome, "tabladeadicion")
    if es_tabla == True:
        operacion("adicion")

    es_tabla = nombre_tabla(welcome, "tabladesustraccion")
    if es_tabla == True:
        operacion("sustraccion")

    es_tabla = nombre_tabla(welcome, "tablademultiplicacion")
    if es_tabla == True:
        operacion("multiplicacion")

    es_tabla = nombre_tabla(welcome, "tabladedivision")
    if es_tabla == True:
        operacion("division")
    
if __name__ == '__main__':
    run()