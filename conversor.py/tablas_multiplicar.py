def nombre_tabla(welcome, tablita):
    welcome = welcome.lower()
    welcome = welcome.replace(" ", "")
    if welcome == tablita:
        return True
    else:
        return False
        

def operacion (operador):
    print("Sobre que tabla de " + operador + " quieres actuar🤔:  ")
    for contador in range (1, 11):
        print (str(contador) + "- " + "tabla del " + str(contador))
    input ("Elige una tabla de " + operador + ": ")


def resolviendo (numero):
    for contador in range (numero, 11):
        print(contador)


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
        if 1:
            resolviendo(1)
        elif 2:
            resolviendo(2)
        elif 3:
            resolviendo(3)      
        elif 4:
            resolviendo(4)
        elif 5:
            resolviendo(5)
        elif 6:
            resolviendo(6)
        elif 7:
            resolviendo(7)
        elif 8:
            resolviendo(8)
        elif 9:
            resolviendo(9)
        elif 10:
            resolviendo(10)
        
    es_tabla = nombre_tabla(welcome, "tabladesustraccion")
    if es_tabla == True:



        es_operacion = operacion("sustraccion", 2)
        if es_operacion == True:
            for contador in range (2, 11):
                print(contador)
        

    es_tabla = nombre_tabla(welcome, "tablademultiplicacion")
    if es_tabla == True:
        operacion("sustraccion")
        pass

    es_tabla = nombre_tabla(welcome, "tabladedivision")
    if es_tabla == True:
        operacion("sustraccion")
        pass
  
if __name__ == '__main__':
    run()
    
