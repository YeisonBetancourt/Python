
def proceso(ejercicio, r1, r2, r3, r4, vt):
    print ("Haz seleccionado el " + ejercicio)
    r1 = r1  
    r2 = r2
    r3 = r3
    r4 = r4
    rt = (r1 + r2 + r3 + r4)
    it = (vt / rt)
    vr1 = (r1 * it)
    vr2 = (r2 * it)
    vr3 = (r3 * it)
    vr4 = (r4 * it)
    vt = str(vr1 + vr2 + vr3 + vr4)
    print ("Este es el resultado final = " +  vt)
def ver_proceso(r1, r2, r3, r4, vt):
    print (r1 = r1)  
    print (r2 = r2)
    print (r3 = r3)
    print (r4 = r4)
    print (rt = (r1 + r2 + r3 + r4))
    print (vt = vt)
    print (it = (vt / rt))
    print (vr1 = (r1 * it))
    print (vr2 = (r2 * it))
    vr3 = (r3 * it)
    vr4 = (r4 * it)
    vt = (vr1 + vr2 + vr3 + vr4)
    

def run():
    taller = ("""Hola profe soy el estudiante Yeison Fernando Gordillo Betancourt del grado 902, he aqui el desarrollo de mi tarea 😅 
    
    1- Primer ejercicio
    2- Segundo ejercicio
    3- Tercer ejercicio
    4- Cuarto ejercicio 
    
    Elige una opcion (1, 2, 3, 4)""")
    taller_electricidad = int(input(taller))
    if taller_electricidad == 1:
        elige = ("""Que deseas ver? 

        1- Resultado final
        2- Proceso
        3- Ambas

        Elige un opcion (1, 2 ,3 ,4) """)

        elige_todo = int(input(elige))
        if elige_todo == 1:
            proceso("ejercicio 1", 20, 700, 80, 10, 56)
        elif elige_todo == 2:
            ver_proceso()


    elif taller_electricidad == 2:
        proceso("ejercicio 2", 50, 60, 30, 773, 70)

    elif taller_electricidad == 3:
        proceso("ejecicio 3", 195, 237, 10, 83, 5)


    elif taller_electricidad == 4:
        proceso("ejercicio 4", 68, 25, 35, 56, 90)

    else: 
        print("Por favor, elije un opcion correcta 💚")

if __name__ == '__main__':
    run()
    









    