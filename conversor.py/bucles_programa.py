def simpl(numerito, numb):
    print("Haz elegido el numero "+ numerito +" este es su valor al cuadrado: ")
    resultado = str(numb*numb)
    print(resultado)
     
def run():
    number = int(input("Escribe un numero: "))
    if number == 1:
        simpl("1", 1)
    elif number == 2:
        simpl("2", 2)





  

# if __name__ == '__main__':
#     run()

# def run():
#     number = int(input("Escribe un numero: "))
#     resultado = str(number*number)
#     print(resultado)

# if __name__ == '__main__':
#     run()
