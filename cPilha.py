# Lab 07 - Pilha
# Criando uma Classe Pilha

#crie a Classe Pilha (cPilha) com os seguintes métodos:
# - push(): Adiciona um elemento no topo da pilha
# - pop(): Remove e retorna o elemento do topo da pilha
# - empty(): Retorna True se a pilha estiver vazia e False caso contrário
# - full(): Retorna True se a pilha estiver cheia e False caso contrário    

# *******************************************************
# ***                                                 ***
# *******************************************************
if __name__ == '__main__':

    numElementos = 10

    pilha = cPilha(numElementos)

    i=100
    while(not pilha.full()):
        pilha.push(i)
        print(f'++ {i}')
        i += 3

    while(not pilha.empty()):
        i = pilha.pop()
        print(f'-- {i}')
