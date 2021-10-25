def r(respuesta, si_no):
    respuesta = respuesta.lower()
    respuesta = respuesta.replace (" ", "")
    if respuesta == si_no:
        return True
    else:
        return False


def ciclo(categoria, nivel, adivinanza, objeto_adivinado ):
    print("-Haz elegido la categoria de " + categoria + " - Que comience el juego! Recuerda que solo tienes 10 oportunidades")
    print(nivel + " nivel: ")
    print(adivinanza)
    for i in range (1,11):
        objeto = input("Escribe: ")
        if objeto != objeto_adivinado:
            print("Nooooo! te quedo mal, este intento numero " + str(i) + " de 10" )
        elif objeto == objeto_adivinado:
            print("FELICITACIONES, LO HAZ LOGRADO! 😜🤤🥳😇🤪😁")
            break        


def run():
    print("""
    --------------------------Bienvenido--------------------------
    ----En esta oportunidad vamos a jugar a adivina adivinador----
    ----------------------------😁💚------------------------------                                 
                    ¿En que consiste el videojuego? 
                    
    Es muy facil😉: tienes que adivinar la adivinanza y solo tienes 
    10 intentos""")
    acepto = input("""
    ----------------------Aceptas el reto?🤔---------------------- 
    
    - Diga "si" para aceptar el reto y continuar... 
    - Diga "no" para denegar el reto y abandonar...
    
    : """)
    decision = r(acepto, "si")
    if decision == True:
        categoria = int(input("""
                 Hay una gran variedad de categorias!!! 🎈

        De acuerdo a tus preferencias elige una... 

        ---------------Que categoria quieres jugar?---------------

        1- Animales
        2- Paises
        3- Ropa y accesorios
        4- Autos deportivos
        5- Peliculas y Series
        6- Alimentos
        7- Frutas
        8- Lenguajes de programacion
        9- Marcas de electrodomesticos
        10- Carreras universitarias
        
        Elige una: """))

        if categoria == 1:
            ciclo("animales", "primer", "Es un animal acuatico, puede vivir en agua dulce o salada, su piel es muy seca y en todo momento su casa esta arriba de el... Que animal sera?", "tortuga")

        elif categoria == 2:
            ciclo("paises", "primer", "Es el pais mas grande del mundo... Que pais sera?", "rusia")
        elif categoria == 3:
            ciclo("ropa y accesorios", "primer", "Es una de las marcas de ropa y accesorrios de todo el mundo su nombre comienza por G... Cual marca sera?", "gucci")
        elif categoria == 4:
            ciclo("autos deportivos", "primer", "Es la marca de autos de la persona mas millonaria del mundo... Que marca sera?", "tesla")
        elif categoria == 5:
            ciclo("peliculas y series", "primer", "Es la pelicula mas taquillera de la historia... Que pelicula sera?", "avatar")
        elif categoria == 6:
            ciclo("alimentos", "primer", "Es un plato muy tipico en Colombia y Venezuela, se come especialmente en las mananas y en las noches con cafe o chocolate... Que alimento sera?", "arepas")
        elif categoria == 7:
            ciclo("frutas", "primer", "Es una fruta pequena, tiene unas pequenas hojas en su parte superior y por ultimo tiene pequenas pepitas amarillas en su cuerpo... Que fruta sera?", "fresa")
        elif categoria == 8:
            ciclo("lenguajes de programacion", "primer","es el mejor lenguaje para el data science", "python")
        elif categoria == 9:
            ciclo("marcas de electrodomesticos", "primer", "Su logo es una manzana mordida... Que marca de electrodomesticos sera?", "apple")
        elif categoria == 10:
            ciclo("carreras universitarias", "primer", "Es una carrera enfocada a la planeacion de la estructura de edificaciones... Que carerra Universitaria sera?", "arquitectura")
        else:
            print("Por favor, elige un valor correcto💚")
            
       
if __name__ == '__main__':
    run()