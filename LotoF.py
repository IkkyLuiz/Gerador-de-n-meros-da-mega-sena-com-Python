import random

class Lotofacil:

    def __init__(self,numero:int):
        self.count = numero 
        self._itered = []

    def __gen_random(self):
        while (rand:=random.randint(1,25)) in self._itered:
            pass
        self._itered.append(rand)
        return rand

    def __iter__(self):
        self._iterations = 1
        return self

    def __next__(self):
        if self._iterations <= self.count:
            self._iterations += 1
            return self.__gen_random()
        else:
            raise StopIteration

    def __repr__(self) -> str:

        return f"Lotofacil({self.count})"

numeros_lotofacil = list(Lotofacil(15))

numeros_lotofacil.sort()

print(numeros_lotofacil)          
