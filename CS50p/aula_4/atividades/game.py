import random

def main():
    dif = level()
    n = random.randint(1, dif)
    game(n)
    



def level():
    while True:
        try:
            n = int(input("Qual o seu nível: "))
            if n <= 0:
                pass
            else:
                return n
        except ValueError:
            pass

def game(n):
    while True:
        try:
            resp = int(input("Qual o número sorteado? "))
            if resp > 0:
                break
            else:
                pass
        except ValueError:
            pass
    if resp > n:
        print("Too large")
    elif resp < n:
        print("Too small")
    else:
        print("Just right!")

main()

