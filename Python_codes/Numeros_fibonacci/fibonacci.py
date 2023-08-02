

def main():
    while True:
        try:
            user_input = int(input("Qual número você quer saber se pertence a sequência de Fibonacci? "))
            break
        except ValueError:
            print('Coloque um número')
    
    print(fib_checker(user_input))


def fib_checker(n_procurado):
    fib_seq = [0,1]
    while n_procurado > fib_seq[-1]:
        new_number = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(new_number)

    if n_procurado == fib_seq[-1]:
        return 'Contém'
    else:
        return f"Não contém, o maior número mais próximo é o {fib_seq[-1]}, enquanto o menor é {fib_seq[-2]}"




if __name__ == "__main__":
    main()