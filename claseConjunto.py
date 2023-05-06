class Conjunto:
    __elementos = []
    def __init__(self):
        self.__elementos = []

    def cargaConjunto(self):
        valor = (input("Ingrese un valor (finalice con 'fin'): "))
        while (valor != 'fin'):
            self.__elementos.append(int(valor))
            valor = (input("Ingrese un valor (finalice con 'fin'): "))
    
    def cantElementos(self):
        return len(self.__elementos)
    
    def getValor(self, pos):
        return self.__elementos[pos]
    
    def mostrarConjunto(self):
        for elem in range (len(self.__elementos)):
            print("Elemento {}: {} ".format(elem, self.__elementos[elem]))

    def buscarElemento(self, belem, conj2):
        i = 0
        bandera = False
        while i < (conj2.cantElementos()) and bandera == False:
            if (belem == conj2.getValor(i)):
                bandera = True
            i += 1
        return bandera


    def __add__(self, conj2):
        suma = Conjunto()
        long1 = self.cantElementos()
        long2 = conj2.cantElementos()

        for elem1 in range(long1):
            suma.__elementos.append(self.__elementos[elem1])

        for elem2 in range (long2):
            if (self.buscarElemento(conj2.getValor(elem2), suma) != True):
                suma.__elementos.append(conj2.getValor(elem2))
        
        return suma.__elementos
 
        
    def __sub__(self, conj2):
        resta = Conjunto()
        long1 = self.cantElementos()
        for elem1 in range (long1):
            bandera = self.buscarElemento(self.__elementos[elem1], conj2)
            if (bandera == False):
                if(self.buscarElemento(self.__elementos[elem1], resta) == False):
                    resta.__elementos.append(self.__elementos[elem1])
        return resta.__elementos


    def __eq__(self, conj2):
        long1 = self.cantElementos()
        long2 = conj2.cantElementos()
        bandera = False
        if (long1 == long2):
            for elem2 in range (long2):
                if (conj2.getValor(elem2) == self.__elementos[elem2]):
                    bandera = True
        else:
            bandera = False
        
        return bandera