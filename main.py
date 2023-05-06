from menu import menuOpciones
from claseConjunto import Conjunto

if __name__ == '__main__':
    
    conjunto1 = Conjunto()
    conjunto2 = Conjunto()

    print("Ingrese los valores para el primer conjunto: ")
    conjunto1.cargaConjunto()
    conjunto1.mostrarConjunto()
    print("Ingrese los valores para el segundo conjunto: ")
    conjunto2.cargaConjunto()
    conjunto2.mostrarConjunto()


    menu = menuOpciones()
    menu.opciones(conjunto1,conjunto2)