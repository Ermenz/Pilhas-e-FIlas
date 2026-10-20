# Lab 07 - Pilhas e Filas
# Criando uma Classe Fila

# Crie a Classe Fila (cFila) com os seguintes métodos:
# - queue(): Adiciona um elemento no final da fila
# - dequeue(): Remove e retorna o elemento do início da fila
# - empty(): Retorna True se a fila estiver vazia e False caso contrário    

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    numElementos = 10

    fila = cFila()

    i=100
    while( numElementos > 0):
        fila.queue(i)
        print(f'++ {i}')
        i += 3
        numElementos -= 1

    while(not fila.empty()):
        i = fila.dequeue()
        print(f'-- {i}')
