taller_electricidad = """Hola profe soy Yeison Fernando Gordillo Betancourt del grado 902, dado que dijiste que podiamoas realizar los ejercicios con cualquier herramienta, pues bueno, lo hice en codigo 😅  

1- Ver el primer ejercicio
2- Ver el segundo ejercicio
3- Ver el tercer ejercicio
4- Ver el cuarto ejercicio


Elige una opcion (1, 2, 3 ,4) """
ejercicios = int(input(taller_electricidad))
if ejercicios == 1:
    print ("Haz seleccionado el primer ejercicio")
    r1 = 690 
    r2 = 500
    r3 = 81
    r4 = 601
    rt = (r1 + r2 + r3 + r4)
    vt = 10
    it = (vt / rt)
    vr1 = (r1 * it)
    vr2 = (r2 * it)
    vr3 = (r3 * it)
    vr4 = (r4 * it)
    vt = (vr1 + vr2 + vr3 + vr4)
    vt = str(vt)
    print ("Este es el resultado final" + " = " + vt)
    ver= """ Quieres ver el proceso?

    1- Si
    2- No

    Elige una opcion (1, 2) """
    ver_proceso = int(input(ver))
    if ver_proceso == 1:
        print ("Haz elegido ver el proceso")
        mostrar_proceso = """
        r1 = 690 
        r2 = 500
        r3 = 81
        r4 = 601
        rt = (r1 + r2 + r3 + r4)
        vt = 10
        it = (vt / rt)
        vr1 = (r1 * it)
        vr2 = (r2 * it)
        vr3 = (r3 * it)
        vr4 = (r4 * it)
        vt = (vr1 + vr2 + vr3 + vr4)"""
        print (mostrar_proceso)










# elif ejercicios == 2:
#     r1 = 372 
#     r2 = 10
#     r3 = 398
#     r4 = 132
#     rt = (r1 + r2 + r3 + r4)
#     vt = 60
#     it = (vt / rt)
#     vr1 = (r1 * it)
#     vr2 = (r2 * it)
#     vr3 = (r3 * it)
#     vr4 = (r4 * it)
#     vt = (vr1 + vr2 + vr3 + vr4)
#     vt = str(vt)
#     print ("Este es el resultado final" + " = " + vt) 

# elif ejercicios == 3:
#     r1 = 542 
#     r2 = 51
#     r3 = 932
#     r4 = 112
#     rt = (r1 + r2 + r3 + r4)
#     vt = 5
#     it = (vt / rt)
#     vr1 = (r1 * it)
#     vr2 = (r2 * it)
#     vr3 = (r3 * it)
#     vr4 = (r4 * it)
#     vt = (vr1 + vr2 + vr3 + vr4)
#     vt = str(vt)
#     print ("Este es el resultado final" + " = " + vt)

# elif ejercicios == 4:
#     r1 = 12 
#     r2 = 50
#     r3 = 818
#     r4 = 61
#     rt = (r1 + r2 + r3 + r4)
#     vt = 68
#     it = (vt / rt)
#     vr1 = (r1 * it)
#     vr2 = (r2 * it)
#     vr3 = (r3 * it)
#     vr4 = (r4 * it)
#     vt = (vr1 + vr2 + vr3 + vr4)
#     vt = str(vt)
#     print ("Este es el resultado final" + " = " + vt)
# else:
#     print("Por favor, elige una opcion correcta💚")

    