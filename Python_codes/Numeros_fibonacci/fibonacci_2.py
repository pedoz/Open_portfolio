def main():
    while True:
        try:
            posicao = int(input("Qual a posição do número? "))
            break
        except ValueError:
            print("Coloque apenas a posição que deseja")
            continue
    
    print(seq_fib(posicao))


def seq_fib(posicao):
    fib = [0,1]
    while True:
        try:
            if len(fib) != posicao:
                new_number = fib[-1] + fib[-2]
                fib.append(new_number)
            else:
                break
        except IndexError:
            continue
    return fib[-1]



if __name__ == "__main__":
    main()