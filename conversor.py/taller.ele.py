def proceso(ejercicio, r1, r2, r3, r4, vt):
    print ("Haz seleccionado el " + ejercicio)
    r1 = r1  
    r2 = r2
    r3 = r3
    r4 = r4
    rt = (r1 + r2 + r3 + r4)
    vt = vt
    it = (vt / rt)
    vr1 = (r1 * it)
    vr2 = (r2 * it)
    vr3 = (r3 * it)
    vr4 = (r4 * it)
    vt = (vr1 + vr2 + vr3 + vr4)
    vt = str(vt)
    print ("Este es el resultado final" + " = " + vt)

def run():
    taller_electricidad = """Hola profe soy Yeison Fernando Gordillo Betancourt del grado 902, dado que dijiste que podiamoas realizar los ejercicios con cualquier herramienta, pu`es bueno, lo hice en codigo 😅 
    
    1- Ver el primer ejercicio
    2- Ver el segundo ejercicio
    3- Ver el tercer ejercicio
    4- Ver el cuarto ejercicio

    Elige una opcion (1, 2, 3 ,4) """
    taller = int(input(taller_electricidad))
    if taller == 1:
        proceso("ejercicio 1",20,700,80,10,56)
    elif taller == 2:
        proceso("ejercicio 2", 50, 60, 30, 773, 70)
    elif taller == 3:
        proceso("ejecicio 3", 195, 237, 10, 83, 5)
    else: 
        print("Por favor, elije un opcion correcta 💚")
    









    