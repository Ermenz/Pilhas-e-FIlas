# Lab06 - Pilha e Fila

## Objetivos:

1. Reforçar os conceitos das estruturas de dados *Pilha* e *Fila*;
2. Codificar os TADs/Classes *Pilha* e *Fila* utilizando a linguagem *Python*;
3. Aprofundar a compreensão dessas estruturas de dados e aplicá-la à resolução de problemas. 

## Exercícios básicos: 

1. Analise o módulo *cPilha.py*. Nele, apenas o código de teste é fornecido. 
Com base nesse código de referência, identifique as operações/métodos esperados na estrutura do TAD/Classe *Pilha* e implemente-os. 

2. Analise o programa *main-Pilha.py* e verifique se a implementação das estruturas de dados do exercício anterior dá suporte a esse código. Caso isso não ocorra, faça os ajustes necessários nos seus módulos e teste-os.

3. Analise o módulo *cFila.py*. Nele, apenas o código de teste é fornecido. Com base nesse código de referência, identifique as operações/métodos esperados na estrutura do TAD/Classe *Fila* e implemente-os. Utilize como estrutura de dados base uma *Lista Simplesmente Encadeada*.

4. Analise o programa *main-Fila.py* e verifique se a implementação da estrutura de dados do exercício anterior dá suporte a esse código. Caso isso não ocorra, faça os ajustes necessários no módulo e teste-o.

5. Crie uma segunda versão do *TAD Fila*, agora utilizando como estrutura de armazenamento base um **vetor circular**. Compare a complexidade dos métodos das duas versões de *Fila*. 

## Exercícios complementares:

> Em todos os exercícios a seguir, sua solução deve utilizar os **TADs Pilha e Fila** criados nesse Lab.

1. As expressões aritméticas seguem regras de precedência entre diferentes operadores, como mostra a Figura 1. Para redefinir a ordem de execução das operações em uma expressão, usam-se **sinais de associação** (também chamados de **sinais de agrupamento** ou **sinais de agregação**). OS sinais mais comuns para esse fim são os **parênteses**, os **colchetes** e as **chaves**, mostrados na Figura 2.  Seu posicionamento, aninhamento e balanceamento devem ser analisados para determinar a validade da expressão aritmética, como na Figura 3. Crie um programa em *Python* que receba como parâmetro de entrada uma expressão aritmética com **parênteses**, **colchetes** e **chaves** e verifique se estão balanceados e aninhados corretamente.

<img src="imgs/Ordem-de-operacoes-nas-expressoes-numericas.webp" width=400> 

*Figura 1 - Regras de precedência para operações aritméticas básicas.*

<img src="imgs/brackets-types.png" width=400> 

*Figura 2 - Sinais de associação presentes em operações aritméticas: parênteses, colchetes e chaves.*

<img src="imgs/parenthesis-checker_thumbnail.webp" width=400>

*Figura 3 - Exemplos de organizações de sinais de associação válidas e inválidas segundo seu posicionamento, aninhamento e balanceamento em uma expressão aritmética.*

2. Expressões aritméticas podem ser escritas em notações diferentes, dependendo do posicionamento do operador em relação aos seus operandos. A Figura 2 mostra as 3 principais notações: **infixa** [4],  **pós-fixa** (ou **polonesa reversa**) [5] e **pré-fixa** (ou **polonesa**) [6]. Implemente um programa em *Python* para conversão entre as notações **infixa** e **posfixa**, que recebe uma expressão aritmética na primeira notação e apresenta sua forma na segunda notação. 

<img src="imgs/pre-in-pos.png" width=400>

*Figura 4 - Expressões aritméticas e suas representações nas notações pré-fixa, infixa e pós-fixa.*

3. Escreva um programa que leia uma frase e determine se ela é um **palíndromo**, desconsiderando espaços, pontuação e diferenças entre letras maiúsculas e minúsculas. Por exemplo, a frase **“A grama é amarga”** deve ser reconhecida como palíndromo, enquanto **“Estrutura de dados”** não deve. O programa deve informar claramente se a frase é ou não um palíndromo e funcionar corretamente com strings vazias ou que contêm apenas símbolos.

4. Crie um programa que receba um número inteiro positivo como entrada e produza a sua representação em binário. Por exemplo, para a entrada **13**, o programa deve retornar **1101**.

5. Considere **n** pessoas numeradas de **1** a **n** dispostas em círculo. A contagem começa na pessoa 1 e, a cada rodada, a **k-ésima** pessoa é eliminada; a contagem reinicia na pessoa imediatamente seguinte à pessoa eliminada. Implemente um programa que receba **n** e **k** e exiba a ordem de eliminação e informe o sobrevivente. Por exemplo, para **n=7** e **k=3**, a eliminação ocorre na ordem 3, 6, 2, 7, 5, 1, restando a pessoa 4.

6. Dado um arquivo *.html* contendo *tags* de abertura e fechamento, como \<div\>, \</div\>, \<p\> e \</p\>, implemente um programa que verifique se todas as *tags* estão corretamente aninhadas e fechadas. O programa deve rejeitar casos como \<b\>\<i\>\</b\>\</i\> ou \<div\>\</span\> informando qual foi o primeiro erro detectado, quando possível. Considere *tags* simples, sem atributos, para manter o foco na estrutura de dados.

7. Dado um inteiro positivo **n**, gere os primeiros **n** números naturais representados em binário, em ordem crescente. Por exemplo, para **n=6**, a saída deve ser: **1, 10, 11, 100, 101 e 110**. O programa deve verificar se **n** é positivo e imprimir os números em linhas separadas.

8. É possível implementar um **TAD Pilha** utilizando exclusivamente 2 **Filas** como estruturas de armazenamento internas? Chamando essa nova pilha de **Pilha-2-Filas**, esse novo TAD deve oferecer as mesmas operações básicas de *empilhar*, *desempilhar*, *verTopo*, *estaVazia* e *tamanho* do TAD original. Caso seja possível, escreva um programa que evidencie o comportamento **LIFO** da **Pilha-2-Filas**, incluindo operações sobre pilha vazia e sequências de empilhamento e desempilhamento intercaladas.

9. Considere um labirinto representado por uma matriz de caracteres, como as mostradas abaixo, em que:
    * **.** representa caminho livre, 
    * **#** representa parede, 
    * **S** é o ponto de partida e 
    * **E** é a saída.
    
    Encontre o menor número de movimentos necessários para sair do labirinto. Os movimentos permitidos são apenas para cima, para baixo, para a esquerda e para a direita, e não é permitido atravessar paredes. O programa deve imprimir o caminho ou a distância mínima ou informar que não existe caminho até a saída.

```python
7 7
#######
#S....#
#.###.#
#.#...#
#.#.#.#
#...#E#
#######
Saida
caminho: (1,1) → (1,2) → (1,3) → (1,4) → (2,4) → (3,4) → (4,4) → (5,4) → (5,5) → (5,6)
```

```python
5 5
#####
#S#.#
#.#.#
#.#E#
#####
Saida
Caminho não existe
```

# Referências:

[1]     Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. Algoritmos – Teoria e Prática. Editora Campus. 3a Edição, 2012..

[2]     Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022. 

[3]     Goodrich, M.T., Tamassia,R., Goldwasser, M.H., **Data Structures and Algorithms in Python**. Wiley. 2013.

[4]     Wikipedia. [**Notação infixa**.](https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_infixa)

[5]     Wikipedia. [**Notação polonesa reversa**.](https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_polonesa_inversa)

[6]     Wikipédia, [**Notação polonesa**](https://pt.wikipedia.org/wiki/Nota%C3%A7%C3%A3o_polonesa)

