import random
import csv


def main():
    word = get_word()
    print(hangman(word))

def get_word():
    word_list = []
    while True:
        try:
            nivel = input("Qual a dificuldade? ")
            if int(nivel) == 0:
                with open('palavras/alea.csv') as file:
                    for line in file:
                        word_list.append(line)
            elif int(nivel) == 1:
                with open('palavras/facil.csv') as file:
                    for line in file:
                        word_list.append(line)
            elif int(nivel) == 2:
                with open('palavras/medio.csv') as file:
                    for line in file:
                        word_list.append(line)
            elif int(nivel) == 3:
                with open('palavras/dificil.csv') as file:
                    for line in file:
                        word_list.append(line)
            else:
                print('Escolha um desses números: 0 - 1 - 2 - 3')
                continue
            break
        except ValueError:
            print('Por favor, insira um número válido.')

    sel_word =  random.choice(word_list)
    return list(sel_word)

def hangman(word):
    letters = word[:-2]
    count = len(word[:-2])
    checker = list()
    n = 6
    wrong_l = list()

    for _ in letters:
        checker.append("_")
    print(*checker, sep = ' ')

    while True:
        if count == 0:
            return 'Parabéns\n'
        if n == 0:
            get_man(n)
            for x in letters:
                print(x.upper(), end = ' ')
            print('')
            return "         Falhou :(\n"
        
        letra = input("Letra:").lower()

        if len(letra) != 1:
            print("Invalido")
        elif letra.isnumeric():
            print("Invalido")
        elif letra.upper() in checker:
            print('Letra repetida')
        elif letra.upper() in wrong_l:
            print('Já não tem essas letras: ', end = '')
            print(*wrong_l, sep = ', ')
        else:
            try:
                j = 0
                for i in range(len(letters)):
                    if letters[i] == letra:
                        count = count - 1
                        checker.pop(i)
                        checker.insert(i, letra.upper())
                        j = j + 1
                    elif ((i + 1) == len(letters)) and (j == 0):
                        n = n - 1
                        wrong_l.append(letra.upper())
                        print(f"\nletras que não tem:", end = ' ')
                        print(*wrong_l, sep = ', ')
                if n == 0:
                    pass
                else:
                    get_man(n)
                    print(*checker, sep = ' ')
                    print(f"\nletras que não tem:", end = ' ')
                    print(*wrong_l, sep = ', ')
                    print('')
            except IndexError:
                print("erro")

def get_man(erros_restantes):
    if erros_restantes == 0:
                return print('''\
   _______________
   |             |
   |             X
   |            /|\\
   |            / \\
  /T\\                 ''', end = '')
    elif erros_restantes == 6:
                return print('''\
   _______________
   |             |
   |             O
   |            
   |            
  /T\\                 ''', end = '')
    elif erros_restantes == 5:
                return print('''\
   _______________
   |             |
   |             O
   |             |
   |            
  /T\\                 ''', end = '')
    elif erros_restantes == 4:
                return print('''\
   _______________
   |             |
   |             O
   |            /|
   |            
  /T\\                 ''', end = '')
    elif erros_restantes == 3:
                return print('''\
   _______________
   |             |
   |             O
   |            /|\\
   |            
  /T\\                 ''', end = '')
    elif erros_restantes == 2:
                return print('''\
   _______________
   |             |
   |             O
   |            /|\\
   |            /
  /T\\                 ''', end = '')
    elif erros_restantes == 1:
        return print('''\
   _______________
   |             |
   |             O
   |            /|\\
   |            / \\
  /T\\                 ''', end = '')


if __name__ == "__main__":
    main()