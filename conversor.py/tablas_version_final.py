def nombre_tabla(var, tablita):
    var = var.lower()
    var = var.replace(" ", "")
    if var == tablita:
        return True
    else:
        return False
        

def suma (numero):
    print ("Tabla del ", numero)
    for i in range (1, 11):
        print(numero,"➕",i,"=", numero+i) 
   

def resta (numero):
    print ("Tabla del ", numero)
    for i in range (2, 11):
        print(numero,"➖",i,"=", i-numero) 


def multiplicacion (numero):
    print ("Tabla del ", numero)
    for i in range (1, 11): 
        print(numero,"✖️",i,"=", numero*i) 


def division (numero):
    print ("Tabla del ", numero)
    for i in range (1, 11):
        print(i,"➗",numero,"=", i/numero) 


def operacion (operador):
    print("Sobre que tabla de " + operador + " quieres actuar🤔:  ")
    for i in range (1, 10):
        print (str(i) + "- " + "tabla del " + str(i))
    numero_elegido = int(input("Elige una tabla de " + operador + ": "))
    return numero_elegido
   

def run():
    welcome = input("""Hola👋, bienvenido a este increible programa donde podras saber:
    
    1- Tablas de adicion ➕
    2- Tablas de sustraccion ➖
    3- Tablas de multiplicacion ✖️
    4- Tablas de division ➗
    
    ¿Que tabla necesitas usar? (EJEMPlO: Tablas de adicion) """)
    es_tabla = nombre_tabla(welcome, "tablasdeadicion")
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
        else:
            print("Por favor elige un valor correcto 💚")    
      
    es_tabla = nombre_tabla(welcome, "tablasdesustraccion")
    if es_tabla == True:
        es_numero = operacion("sustraccion")
        if es_numero == 1:
            resta(1)
        elif es_numero == 2:
            resta(2)
        elif es_numero == 3:
            resta(3)
        elif es_numero == 4:
            resta(4)
        elif es_numero == 5:
            resta(5)
        elif es_numero == 6:
            resta(6)
        elif es_numero == 7:
            resta(7)
        elif es_numero == 8:
            resta(8)
        elif es_numero == 9:
            resta(9)
        else:
            print("Por favor elige un valor correcto 💚")

        
    es_tabla = nombre_tabla(welcome, "tablasdemultiplicacion")
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
        else:
            print("Por favor elige un valor correcto 💚")

    es_tabla = nombre_tabla(welcome, "tablasdedivision")
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
        else:
            print("Por favor elige un valor correcto 💚")
    else:
        print("Por favor elige un valor correcto 💚")


if __name__ == '__main__':
    run()