def nombre_tabla(welcome, tablita):
    welcome = welcome.lower()
    welcome = welcome.replace(" ", "")
    if welcome == tablita:
        return True
    else:
        return False
        

def operacion (operador, number):
    print("Sobre que tabla de " + operador + " quieres actuar🤔:  ")
    for contador in range (1, 11):
        print (str(contador) + "- " + "tabla del " + str(contador))
    elige_tabla = int(input("Elige una tabla de " + operador + ": "))
    if elige_tabla == number:
        return True
    else:
        return False


def run():
    welcome = input("""Hola👋, bienvenido a este increible programa donde podras saber:
    
    1- Tabla de adicion
    2- Tabla de sutracion
    3- Tabla de multiplicacion
    4- Tabla de la division 
    
    ¿Que tabla necesitas usar? (EJEMPlO: Tabla de adicion) """)
    es_tabla = nombre_tabla(welcome, "tabladeadicion")
    if es_tabla == True:
        es_operacion = operacion("adicion", 1)
        if es_operacion == True:
            for contador in range (1, 11):
                print(contador)

    es_tabla = nombre_tabla(welcome, "tabladesustraccion")
    if es_tabla == True:
        es_operacion = operacion("sustraccion", 1)
        if es_operacion == True:
            for contador in range (1, 11):
                print(contador)
        

    es_tabla = nombre_tabla(welcome, "tablademultiplicacion")
    if es_tabla == True:
        operacion("sustraccion")
        pass

    es_tabla = nombre_tabla(welcome, "tabladedivision")
    if es_tabla == True:
        operacion("sustraccion")
        pass

    else:
        print("Elige una opcion correcta, por favor 💚")
if __name__ == '__main__':
    run()