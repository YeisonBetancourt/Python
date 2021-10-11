def nombre_tabla(welcome, tablita):
    welcome = welcome.lower()
    welcome = welcome.replace(" ", "")
    if welcome == tablita:
        return True
    else:
        return False
        

def resolviendo (numero, rango, add):
    for contador in range (numero, rango):
        print(contador + add)


def operacion (operador):
    print("Sobre que tabla de " + operador + " quieres actuar🤔:  ")
    for contador in range (1, 10):
        print (str(contador) + "- " + "tabla del " + str(contador))
    numero_elegido = int(input("Elige una tabla de " + operador + ": "))
    return numero_elegido


def run():
    welcome = input("""Hola👋, bienvenido a este increible programa donde podras saber:
    
    1- Tabla de adicion
    2- Tabla de sustraccion
    3- Tabla de multiplicacion
    4- Tabla de la division 
    
    ¿Que tabla necesitas usar? (EJEMPlO: Tabla de adicion) """)
    es_tabla = nombre_tabla(welcome, "tabladeadicion")
    if es_tabla == True:
        es_numero = operacion("adicion")
        if es_numero == 1:
            resolviendo(0, 10, +1)
        elif es_numero == 2:
            resolviendo(1,11, +1)
        elif es_numero == 3:
            resolviendo(2,12, +1)
        elif es_numero == 4:
            resolviendo(3,13, +1)
        elif es_numero == 5:
            resolviendo(4,14, +1)
        elif es_numero == 6:
            resolviendo(5,15, +1)
        elif es_numero == 7:
            resolviendo(6,16, +1)
        elif es_numero == 8:
            resolviendo(7,17, +1)
        elif es_numero == 9:
            resolviendo(8,18, +1)                 
        else:
            print("Elija una opcion correcta 💚")


    es_tabla = nombre_tabla(welcome, "tabladesustraccion")
    if es_tabla == True:
        es_numero = operacion("sustraccion")
        if es_numero == 1:
            resolviendo(1, 10)
        elif es_numero == 2:
            resolviendo(1,10)
        elif es_numero == 3:
            resolviendo(1,10)
        elif es_numero == 4:
            resolviendo(1,10)
        elif es_numero == 5:
            resolviendo(1,10)
        elif es_numero == 6:
            resolviendo(1,10)
        elif es_numero == 7:
            resolviendo(1,10)
        elif es_numero == 8:
            resolviendo(1,10)
        elif es_numero == 9:
            resolviendo(1,10)                 
        else:
            print("Elija una opcion correcta 💚")

    es_tabla = nombre_tabla(welcome, "tablademultiplicacion")
    if es_tabla == True:
        es_numero = operacion("multiplicacion")
        if es_numero == 1:
            resolviendo(0, 10, * 1)
        elif es_numero == 2:
            resolviendo(1,11, * 1)
        elif es_numero == 3:
            resolviendo(2,12, * 1)
        elif es_numero == 4:
            resolviendo(3,13, * 1)
        elif es_numero == 5:
            resolviendo(4,14, * 1)
        elif es_numero == 6:
            resolviendo(5,15, * 1)
        elif es_numero == 7:
            resolviendo(6,16, * 1)
        elif es_numero == 8:
            resolviendo(7,17, * 1)
        elif es_numero == 9:
            resolviendo(8,18, * 1)                 
        else:
            print("Elija una opcion correcta 💚")

    es_tabla = nombre_tabla(welcome, "tabladedivision")
    if es_tabla == True:
        operacion("division")
    
if __name__ == '__main__':
    run()