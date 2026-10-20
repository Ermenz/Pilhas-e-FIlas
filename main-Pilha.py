# ##################################################
# Programa de teste para Pilha e Fila
# ##################################################

import cPilha

import sys
import random
import math

from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    numElementos = 20

    pilha = cPilha.cPilha(numElementos)

    i=100
    while(not pilha.full()):
        pilha.push(i)
        print(f'++ {i}')
        i += 3

    while(not pilha.empty()):
        i = pilha.pop()
        print(f'-- {i} {j}')
