# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM
import random
numero_aleatorio = random.randint(0, 5)
tentativa = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 5): "))
if tentativa == numero_aleatorio:
    print(f"Parabéns! Você acertou. O número era {numero_aleatorio}. Você venceu!")
else:
    print(f"Você errou. O número escolhido pelo computador era {numero_aleatorio}. Você perdeu.")