
import random

class NumerosMegaSena:

    def __init__(self,numero:int):
        self.count = numero 
        self._itered = []

    def __gen_random(self):
        while (rand:=random.randint(1,60)) in self._itered:
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

        return f"NumerosMegaSena({self.count})"

numeros_mega = list(NumerosMegaSena(6))

numeros_mega.sort()

print(numeros_mega)          
