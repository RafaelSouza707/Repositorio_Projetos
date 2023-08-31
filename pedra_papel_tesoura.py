from random import randint
from time import sleep

#Menu para acessar as opçoes
itens =  ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opçoes:
      [0] Pedra
      [1] Papel
      [2] Tesoura''')
jogador = int(input('Qual será sua jogada? '))
print('-' * 30)
print('Computador Jogou {}' .format(itens[computador]))
print('Jogador Jogou {}' .format(itens[jogador]))
print('-' * 30)


#Funcao para organizar espaçamentos
def linhas_Jogo():
    print('=====' * 3)

#Codigo da funcionalidade do jogo
sleep(1)
if jogador ==  computador:
    linhas_Jogo()
    print('Foi empate!')
    linhas_Jogo()
elif jogador == 0:
    linhas_Jogo()
    if computador == 1:
        print('Voce perdeu!')
    elif computador == 2:
        print('Voce venceu!')
    else:
        print('Jogada invalida!')
    linhas_Jogo()
elif jogador == 1:
    linhas_Jogo()
    if computador == 2:
        print('Voce perdeu!')
    elif computador == 0:
        print('Voce venceu!')
    linhas_Jogo()
elif jogador == 2:
    linhas_Jogo()
    if computador == 0:
        print('Voce perdeu!')
    elif computador == 1:
        print('Voce venceu!')
    linhas_Jogo()