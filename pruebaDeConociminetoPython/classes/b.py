#Importaciones
import random

#Creacion de la clase
class B:
    #Atributos
    b = []
    first = int()
    last = int()
    prime = int()
    even = int()
    odd = int()
    firstPosition = int()
    lastPosition = int()

    #Constructor
    def __init__(self):
        ...

    ##METODOS##
    
    #Generar numeros
    def generate(self):
        self.b.clear()
        self.prime = 0
        self.even = 0
        self.odd = 0
        for i in range(0,600):
            counter = 0
            #Llenar el arreglo
            self.b.append(random.randint(1,100))
            #Calcular el primer numero
            if i == 0:
                self.first = self.b[i]
                self.firstPosition = i
            #Calcular el ultimo numero
            if i == 99:
                self.last = self.b[i]
                self.lastPosition = i
            #Calcular pares
            if self.b[i] % 2 == 0:
                self.even +=  1
            #Calcular impares
            if self.b[i] % 2 != 0:
                self.odd += 1
            #Calcular primos
            for j in range(1, self.b[i]+1):
                if self.b[i] % j == 0:
                    counter += 1
                if counter > 2:
                    self.prime += 1
                    break
    
    #Es primo
    def isEven(self, num):
        if num % 2 == 0:
            return True
        else:
            return False
    
    #Es inpar
    def isOdd(self, num):
        if num % 2 != 0:
            return True
        else:
            return False
        
    #Es primo
    def isPrime(self, num):
        counter = 0
        isPrime = True
        if num == 1 or num == 0:
            isPrime = False
        for i in range(1, num+1):
                if num % i == 0:
                    counter += 1
                if counter > 2:
                    isPrime = False
                    break
        return isPrime
                    
        
#Master                
master = B()








