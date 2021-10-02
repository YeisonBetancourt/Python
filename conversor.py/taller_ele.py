def proceso(ejercicio, r1, r2, r3, r4, vt):
    print (ejercicio)
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
def que_deseas():
    print("""Que deseas ver? 

        1- Resultado final
        2- Proceso
        3- Ambas
    """)  
def ver_proceso():
    print ("Este es el proceso 🔎")
    print ("""r1 = r1  
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
    print ("Este es el resultado final = " +  vt)""")
def run():
    taller = ("""Hola profe soy el estudiante Yeison Fernando Gordillo Betancourt del grado 902, he aqui el desarrollo de mi tarea 😅 
    
    1- Primer ejercicio
    2- Segundo ejercicio
    3- Tercer ejercicio
    4- Cuarto ejercicio 
    
    Elige una opcion (1, 2, 3) """)
    taller_electricidad = int(input(taller))
    if taller_electricidad == 1:
        que_deseas()
        elige_todo = int(input("Elige una opcion (1, 2, 3, 4) "))
        if elige_todo == 1:
            proceso("Haz seleccionado el ejercicio 1", 20, 700, 80, 10, 56)
        elif elige_todo == 2:
            ver_proceso()
        elif elige_todo == 3:
            ver_proceso()
            proceso("Y este es el resultado", 20, 700, 80, 10, 50)
        else:
            print("Por favor, elige una opcion correcta")
    elif taller_electricidad == 2:
        que_deseas()
        elige_todo2 = int(input("Elige una opcion (1, 2, 3, 4) "))
        if elige_todo2 == 1:
            proceso("Haz seleccionado el ejercicio 2", 50, 60, 30, 773, 70)
        elif elige_todo2 == 2:
            ver_proceso()
        elif elige_todo2 == 3:
            ver_proceso()
            proceso("Y este es el resultado", 50, 60, 30, 773, 70)
        else:
            print("Por favor, elige una opcion correcta")
    elif taller_electricidad == 3:
        que_deseas()
        elige_todo3= int(input("Elige una opcion (1, 2, 3, 4) "))
        if elige_todo3 == 1:
            proceso("Haz seleccionado el ejercicio 3", 195, 237, 10, 83, 5)
        elif elige_todo3 == 2:
            ver_proceso()
        elif elige_todo3 == 3:
            ver_proceso()
            proceso("Y este es el resulatado", 195, 237, 10, 83, 5)
        else:
            print("Por favor, elige una opcion correcta")
    elif taller_electricidad == 4:
        que_deseas()
        elige_todo4 = int(input("Elige una opcion (1, 2, 3, 4) "))
        if elige_todo4 == 1:
            proceso("Haz seleciconado el ejercicio 4", 68, 25, 35, 56, 90)
        elif elige_todo4 == 2:
            ver_proceso()
        elif elige_todo4 == 3:
            ver_proceso()
            proceso("Y este es el reusltado", 68, 25, 35, 56, 90)
        else:
            print("Por favor, elige una opcion correcta")
    else: 
        print("Por favor, elige un opcion correcta 💚")

if __name__ == '__main__':
    run()