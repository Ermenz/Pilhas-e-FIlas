# ##################################################
# Programa de teste para Pilha e Fila
# ##################################################

import cFila

import random

from datetime import datetime

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    random.seed(int(datetime.now().strftime('%H%M%S')))

    numElementos = 20

    fila = cFila.cFila()

    i=100
    k = 0
    while(k < numElementos and not fila.full()):
        fila.queue(i)
        print(f'++ {i}')
        i += 3
        k += 1

    while(not fila.empty()):
        i = fila.dequeue()
        print(f'-- {i}')