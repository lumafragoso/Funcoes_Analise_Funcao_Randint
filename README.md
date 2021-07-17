# Funcoes_Analise_Funcao_Randint
Assessment activity of the 1º period of IT Bachelor on Functions in Python / Atividade avaliativa do 1º periodo do Bacharelado em TI sobre Funções em Python

## Análise Função Randint

### Goal / Objetivo

In the question of the guessing game we use the randint function that randomly chooses a certain integer within a given range as a parameter. We saw that it is possible for a number to be chosen several times in a row, as if the choice were "addicted". To analyze whether or not there is bias in this randint function, we must consider a relatively high number of number choices and count how many times each number was chosen. This count by chosen number (repeat) must be close to each other.
So, make a program that asks the user for a range of values ​​and how many random number choices from that range he wants to make, outputting the amount each number in the range was chosen for.

Na questão do jogo da advinhação usamos a função randint que escolhe aleatoriamente um determinado número inteiro dentro de um intervalo informado como parâmetro. Vimos que é possível um número ser escolhido diversas vezes seguidas, como se a escolha estivesse "viciada". Para analisar se há vício ou não nesta função randint, devemos considerar uma quantidade relativamenet alta de escolhas dos números e contar quantas vezes cada número foi escolhido. Esta contagem por número escolhido (repetição) devem ser próximas umas das outras.
Assim, faça um programa que pede ao usuário um intervalo de valores e quantas escolhas aleatórias de números deste intervalo deseja fazer, dando como saída a quantidade em que cada número do intervalo foi escolhido.

1. Exemple / Exemplo
```py

Inteiro inicial do intervalo? 0
Inteiro final do intervalo? 1
Quantidade de escolhas? 100
Contagem de escolhas:
0 - 49
1 - 51
```
