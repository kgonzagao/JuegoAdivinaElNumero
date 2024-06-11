# importamos la libreria random
from random import randrange

# Creamos la clase Aleatorio para que nos genere el numero
# aleatorio para adivinar
class Aleatorio():
    def __init__(self,pNumero1,pNumero2):
        self.numero1=pNumero1
        self.numero2=pNumero2

    def __str__(self) -> str:
        return str(randrange(self.numero1,self.numero2))

# Creamos la clase rango para que nos genere la tupla de los rango
# para adivinar y tambien creamos la funcion reemplazar
# para asignar x a los numeros que no hemos acertado
class Rango():
    def numeros(self,pN1,pN2):
        if pN2>pN1:
            for i in range(pN1,pN2):
                tupla = tuple(range(1, i + 1))
            return tupla
        else:
            return "Numeros fuera de rangos"

    def reemplazar_x(self,pTupla,pCondicion):
        lista = list(pTupla)

        for i in range(len(lista)):
            if lista[i]==int(pCondicion):
                lista[i]='X'
        return tuple(lista)