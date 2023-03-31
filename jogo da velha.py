import random
import sys

choices = 'pedra papel tesoura'.split()

def winner(playerChoice, computerChoice):
    if playerChoice == computerChoice:
        print('O jogo terminou em empate.')
    elif playerChoice == 'pedra' and computerChoice == 'tesoura':
        print('Você ganhou!')
    elif playerChoice == 'papel' and computerChoice == 'pedra':
        print('Você ganhou!')
    elif playerChoice == 'tesoura' and computerChoice == 'papel':
        print('Você ganhou!')
    else:
        print('O Computador ganhou!')

while True:
    print('Escolha pedra, papel ou tesoura.')
    playerChoice = input().lower()
    if playerChoice not in choices:
        print('Escolha pedra, papel ou tesoura.')
        playerChoice = input().lower()
    computerChoice = random.choice(choices)
    print('Você escolheu %s, o computador escolheu %s.' % (playerChoice, computerChoice))
    winner(playerChoice, computerChoice)
    print('Gostaria de jogar denovo? (sim ou não)')
    if not input().lower().startswith('s'):
        sys.exit()
