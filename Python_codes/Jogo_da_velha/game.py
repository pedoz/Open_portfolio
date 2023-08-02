import random

def main():
    n = [0,1,2,3,4,5,6,7,8,9]
    while True:
        jogo = f'''
        {n[1]} | {n[2]} | {n[3]}
        -----------
        {n[4]} | {n[5]} | {n[6]} 
        -----------
        {n[7]} | {n[8]} | {n[9]}
        '''
        print(jogo)
        
        n = jogada_jogador(n)
        if end_game(n):
            print("Venceu")
            break
        elif draw(n):
            print("Empate")
            break
        n = jogada_maquina(n)
        if end_game(n):
            print('Perdeu')
            break


def end_game(n):
    if (n[1] == n[2] == n[3]) or \
    (n[4] == n[5] == n[6]) or \
    (n[7] == n[8] == n[9]) or \
    (n[1] == n[4] == n[7]) or \
    (n[2] == n[5] == n[8]) or \
    (n[3] == n[6] == n[9]) or \
    (n[1] == n[5] == n[9]) or \
    (n[3] == n[5] == n[7]):
        return True
        

def draw(n):
    if all([isinstance(item, str) for item in n[1:]]):
        return True


def jogada_jogador(n):
    x = 'X'
    o = 'O'
    symbol = x
    while True:
        try:
            j_jogador = int(input("Qual posição tu quer colocar? "))
            if 9 >= j_jogador >= 1:
                for number in n:
                    if j_jogador == number:
                        n.pop(number)
                        n.insert(number, symbol)
                        return n
                    elif number == len(n)-1:
                        print('Coloque uma posição válida, por favor')
            else:
                print('Coloque uma posição válida, por favor')
                pass
        except ValueError:
            print('Coloque uma posição válida, por favor')

def jogada_maquina(n):
    x = "X"
    o = "O"
    symbol = o
    while True:
        try:
            jogada = random.choice(n)
            if jogada == 'O' or jogada == 'X' or jogada == 0:
                pass
            else:
                for number in n:
                    if number == jogada:
                        n.pop(number)
                        n.insert(number, symbol)
                        return n
        except ValueError:
            print("Erro indesejado")


if __name__ == '__main__':
    main()