def nombre_tabla(welcome, tablita):
    welcome = welcome.lower()
    welcome = welcome.replace(" ", "")
    if welcome == tablita:
        return True
    else:
        return False
        

def suma (numero):
    for i in range (1, 10):
        print(i+ numero)


def resta (numero, rango):
    for i in range (numero, rango):
        print(i- 1)


def multiplicacion (numero):
    for i in range (1, 11):
        print(i* numero)


def division (numero):
    for i in range (1, 11):
        print(i/ numero)


def operacion (operador):
    print("Sobre que tabla de " + operador + " quieres actuar🤔:  ")
    for i in range (1, 10):
        print (str(i) + "- " + "tabla del " + str(i))
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
            suma(1)  
        elif es_numero == 2:
            suma(2)
        elif es_numero == 3:
            suma(3)
        elif es_numero == 4:
            suma(4)
        elif es_numero == 5:
            suma(5)
        elif es_numero == 6:
            suma(6)
        elif es_numero == 7:
            suma(7)
        elif es_numero == 8:
            suma(8)
        elif es_numero == 9:
            suma(9)
            
            
    es_tabla = nombre_tabla(welcome, "tabladesustraccion")
    if es_tabla == True:
        es_numero2 = operacion("sustraccion")
        if es_numero2:
            resta(1,10)

        
    es_tabla = nombre_tabla(welcome, "tablademultiplicacion")
    if es_tabla == True:
        es_numero = operacion("multiplicacion")
        if es_numero == 1:
            multiplicacion(1)
        elif es_numero == 2:
            multiplicacion(2)
        elif es_numero == 3:
            multiplicacion(3)
        elif es_numero == 4:
            multiplicacion(4)
        elif es_numero == 5:
            multiplicacion(5)
        elif es_numero == 6:
            multiplicacion(6)
        elif es_numero == 7:
            multiplicacion(7)
        elif es_numero == 8:
            multiplicacion(8)
        elif es_numero == 9:
            multiplicacion(9)

    es_tabla = nombre_tabla(welcome, "tabladedivision")
    if es_tabla == True:
        es_numero = operacion("division")
        if es_numero == 1:
            division(1)
        elif es_numero == 2:
            division(2)
        elif es_numero == 3:
            division(3)
        elif es_numero == 4:
            division(4)
        elif es_numero == 5:
            division(5)
        elif es_numero == 6:
            division(6)
        elif es_numero == 7:
            division(7)
        elif es_numero == 8:
            division(8)
        elif es_numero == 9:
            division(9)


if __name__ == '__main__':
    run()