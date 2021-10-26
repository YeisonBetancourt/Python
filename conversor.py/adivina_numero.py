import random 
def salir():
    run()
    

def palabra(welcome, ask):
    welcome = welcome.lower()
    welcome = welcome.replace(" ","")
    if welcome == ask:
        return True
    else:
        return False



def ciclo(vidas, nivel):
    numero_elegido = int(input("Recuerda que solo tienes " + str(vidas) + " vidas ❤❤❤❤ Escribe un numero: "))
    numero_aleatorio = random.randint(1, 50)
    for i in range(1, vidas):
        if numero_elegido == numero_aleatorio:
            print("Haz ganado!!! 🤪🤪🤪")
            input("Deseas continuar con el nivel numero " + str(nivel) + "(si/no) ")
        elif numero_elegido < numero_aleatorio:
            print("Busca un numero mas grande... Este es tu intento numero " + str(i) + " de " + str(vidas))
        else:
            print("Busca un numero mas pequeno... Este es tu intento numero " + str(i) + " de " + str(vidas))
        numero_elegido = int(input("Elige otro numero: "))


def run():

    welcome = input(""" 
    -------------------Bienvenido a adivina el numero😀------------------ 
    
    En que consiste este videojuego? Bueno trata de adivinar un numero entre 1 y 100
    
    Estas listo?(Si/No): """)
    if palabra(welcome, "si"):
        ciclo(10, 2)
        ciclo(5, 3)
        ciclo(3, 4)
        ciclo(2, 5)
        ciclo(1, 6)






    # 
    #     numero_elegido = int(input("""
    #     Recuerda que solo tienes 10 vidas ❤❤❤❤❤

    #     Ahora si empecemos! 
        
    #     Escribe un numero: """))
        # numero_aleatorio = random.randint(1, 100)
        # for i in range(1, 11):
        #     if numero_elegido == numero_aleatorio:
        #         print("Haz ganado!!! 🤪🤪🤪")
        #     if numero_elegido == numero_aleatorio:
        #         two = input("Deseas continuar con el nivel nuemro 2? (si/no) ")
        #         if two == "si":
        #             print("Hola")
        #         else:
        #             print("Hasta la vista") 
        #     elif numero_elegido < numero_aleatorio:
        #         print("Busca un numero mas grande... Este es tu intento numero " + str(i) + " de 10")
        #     else:
        #         print("Busca un numero mas pequeno... Este es tu intento numero " + str(i) + " de 10")
        #     numero_elegido = int(input("Elige otro numero: "))
    else:
        print("Por favor, escribe (si o no )")

if __name__ == '__main__':
    run()