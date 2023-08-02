import random


def main():
    rodadas = 10
    score = 0
    level = get_level()
    while rodadas > 0:
        x, y = generate_integer(level)
        teste = maths(x, y)
        if teste == True:
            score = score + 1
            rodadas = rodadas - 1
        else:
            rodadas = rodadas - 1
    print(score)


def generate_integer(level):
    
    n1 = 0 + ((level - 1) * 10)
    if level == 1:
        n2 = 9
    elif level == 2:
        n2 = 99
    else:
        n2 = 999
    x = random.randint(n1,n2)
    y = random.randint(n1,n2)
    return x, y
    
def maths(x, y):
    n = 3
    while n > 0:
        try:    
            r = int(input(f"{x} + {y} = "))
            if x + y == r:
                return True
            elif n == 1:
                print(f"{x} + {y} = {x+y}")
                return False
            else:
                print("EEE")
                n = n - 1
        except ValueError:
            print("EEE")
            n = n - 1

def get_level():
    while True:
        try:
            level = int(input("Qual seu nível? "))
            if level == 1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass

if __name__ == "__main__":
    main()