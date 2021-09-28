from os import DirEntry


welcome = """Hola bienvenido a @buenoslibros.com, estos el top5 libros mas vendidos de la historia.

1- El venderdor Millonario
2- Piense y hagase rico
3- Cien anos de soledad
4- El club de las 5 de la manana
5- Habitos de ricos

Que libro quieres comprar? (1, 2, 3, 4, 5):  """
libro = int(input(welcome))
if libro == 1:
    print ("Haz seleccionado la opcion 1")
    print ("Felicitaciones, esta es una muy buena eleccion")
    metodo_pago = ("""Lo vas a comprar con:

    1- Tarjeta de debito
    2- Efectivo 
    3- tarjeta de credito 

    Elige un metodo de compra (1, 2, 3)  """)
    sell = int(input(metodo_pago))
    if sell == 1:
        input ("Cual es tu numero de cuenta?  ")
        print ("Estamos a poco pasos de efectuar la venta...")
        llegada = (""" Opciones de domicilio
        1- Domicilio
        2- Oficina
        3- Nustras instalaciones

        Elige una opcion (1, 2, 3) """)
        lugar_definido = int(input(llegada))
        if lugar_definido == 1:
            input ("Cual es la dirreccion? ")
            print ("""La venta se ha efectuado exitosamente, en 5 dias habiles el libro estara en tu domicilio
            
            MUCHAS GRACIAS POR TU COMPRA 💚""")
        elif lugar_definido == 2:
            input ("Cual es la dirreccion de tu oficina? ")
            print ("""La venta se ha efectuado exitosamente, en 5 dias habiles el libro estara en tu oficina

            MUCHAS GRACIAS POR TU COMPRA 💚""")
        elif lugar_definido == 3:
            oficinas = ("""En que ciudad te encuentras?
            
            1- Bogota
            2- Medellin
            3- Villavicencio
            4- Tunja
            5- Manizales
            
            Elige una opcion (1, 2, 3, 4, 5 ) """)
            destino_final = int(input(oficinas))
            if destino_final == 1:
                print ("""Haz elegido Bogota
                Tenemos una oficina en el barrio Kennedy""")
                dirrecion_oficina = """Te sirve esta oficina?

                1- Si
                2- No

                Elige una opcion (1, 2) """
                entrega_pedido = int(input(dirrecion_oficina))
                if entrega_pedido == 1:
                    print (""" La venta se ha efectuado exitosamente, en 3 dias habiles podras venir a nuestras instalaciones para recoger tu libro
            
                    MUCHAS GRACIAS POR TU COMPRA 💚""")
                elif entrega_pedido == 2:
                    print ("Elige alguna de las otras 2 opciones, el domicilio es totalmente gratis, aunque se demorara 2 dias mas")
                else:   
                    print ("Por favor elije una modalidad correcta")

            elif destino_final == 2:
                print ("""Haz elegido Medellin
                Tenemos una oficina en el Poblado""")
                
                oficina_poblado = """Te sirve esta oficina?

                1- Si
                2- No

                Elige una opcion (1, 2) """
                entrega_poblado = int(input(oficina_poblado))
                if entrega_poblado == 1:
                    print (""" La venta se ha efectuado exitosamente, en 3 dias habiles podras venir a nuestras instalaciones para recoger tu libro
            
                    MUCHAS GRACIAS POR TU COMPRA 💚""")
                elif entrega_poblado == 2:
                    print ("Elige alguna de las otras 2 opciones, el domicilio es totalmente gratis, aunque se demorara 2 dias mas")
                else:
                    print ("Por favor elije una modalidad correcta")
            elif destino_final == 3:
                print ("""Haz elegido Villavicencio.
                Tenemos una oficina en el barrio Porvenir """)
                oficina_villavicencio = """Te sirve esta oficina

                1- Si
                2- No
                
                Elije una opcion (1, 2) """

                pedido_villavicencio = int(input(oficina_villavicencio))
                if pedido_villavicencio == 1:
                    print (""" La venta se ha efectuado exitosamente, en 3 dias habiles podras venir a nuestras instalaciones para recoger tu libro
            
                    MUCHAS GRACIAS POR TU COMPRA 💚""")
                elif pedido_villavicencio == 2:
                    print ("Elige alguna de las otras 2 opciones, el domicilio es totalmente gratis, aunque se demorara 2 dias mas")
                else:
                    print ("Por favor elije una modalidad correcta")
            elif destino_final == 4:
                print ("""Haz elegido Tunja 
                Tenemos una oficina en el barrio Atarazana""")
                oficina_tunja = """Te sirve esta oficina?

                1- Si
                2- No

                Elije una opcion (1, 2) """
                pedido_tunja = int(input(oficina_tunja))   
                if pedido_tunja == 1:
                    print (""" La venta se ha efectuado exitosamente, en 3 dias habiles podras venir a nuestras instalaciones para recoger tu libro
            
                    MUCHAS GRACIAS POR TU COMPRA 💚""")
                elif pedido_tunja == 2:
                    print ("Elige alguna de las otras 2 opciones, el domicilio es totalmente gratis, aunque se demorara 2 dias mas")
                else:
                    print ("Por favor elije una modalidad correcta")
            elif destino_final == 5:
                print ("""Haz elegido Manizales
                Tenemos una oficina en el barrio Palermo""")
                oficina_manizales = """ Te sirve esta oficina?

                1- Si
                2- No

                Elige una opcion (1, 2) """
                pedido_manizales = int(input(oficina_manizales))
                if pedido_manizales == 1:
                    print (""" La venta se ha efectuado exitosamente, en 3 dias habiles podras venir a nuestras instalaciones para recoger tu libro
            
                    MUCHAS GRACIAS POR TU COMPRA 💚""")
                elif pedido_manizales == 2:
                    print ("Elige alguna de las otras 2 opciones, el domicilio es totalmente gratis, aunque se demorara 2 dias mas")
                else:
                    print ("Por favor elije una modalidad correcta")
    elif sell == 2:
        pago = """Puedes pagar en efectivo en cualquiera de estas 3 empresas

        1- Efecty
        2- Servientrega
        3- Baloto

        Con que empresa quieres hacer la transaccion?

        Elige una opcion (1, 2, 3) """
        transaccion = int(input(pago))
        if transaccion == 1:
            print("Haz seleccionado Efecty")
            pagar = """Si hacemos la factura ahora mismo tendras 12 horas disponibles para acercarte a un corresponsal efecty y hacer la transaccion ¿Que dices?

            1- Acepto
            2- No acepto
             
            Elige una opcion (1, 2)"""
            pago_concretado = int(input(pagar))
            if pago_concretado == 1:
                print ("Es5tamos a unos pasos de generar tu factura")
                nombres = input("Cuales son tus nombres y apellidos?")
                gmail = input("Cual es tu gmail? ")
                numero = input("Cual es tu numero telefonico")
                print (""" La factura se ha efectuado exitosamente y se ha enviado a tu correo electronico, tienes 12 horas a partir de hora para hacer el pago
            
                MUCHAS GRACIAS POR TU COMPRA 💚""")











                        
                
          

       

