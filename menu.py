class menuOpciones:
    def __init__(self, opcion='0'):
        self.__opcion = opcion

    def opciones(self, conj1, conj2):

        while self.__opcion != 4:
            print("Menu de opciones: ")
            print("1) - Union de dos conjuntos")
            print("2) - Diferencia de dos conjuntos")
            print("3) - Verificar si dos conjuntos son iguales")
            print("4) - Salir")
            self.__opcion = int(input("Seleccione una opcion: "))
            
            if self.__opcion == 1:
                suma = conj1 + conj2
                print("El resultado de la union es: {}".format(suma))
            
            elif self.__opcion == 2:
                resta = conj1 - conj2
                print("La resultado de la diferencia es: {}".format(resta))

            elif self.__opcion == 3:
                igual = conj1 == conj2
                if igual == True:
                    print("Conjunto 1 y Conjunto 2 son iguales")

                else:
                    print("Conjunto 1 y Conjunto 2 son distintos")

            elif self.__opcion == 4:
                print("FIN")

            else:
                print("Opcion invalida, ingrese otra")