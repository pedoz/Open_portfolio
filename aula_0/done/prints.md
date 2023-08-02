# Programação CS50

´ PRINT FUNCTION ´
, = separa parametros, e separa os argumentos com espaço

name = input("What's your name?")
print("Hello, " + name)
´or print("Hello, ",end+"")´
´print(name)´


print('Hello, "friend"') -> ' ou " separa e lê como tu quer o print
ou
print("Hello, \"friend\"")

print("Hello,",name +"!")

----------------------
.strip = remove os espaços das strings da esquerda e da direita, colocando 'r' ou 'l' .strip, ele só tira da direita/esquerda
name = name.strip()

.capitalize = Apenas a primeira letra fica maiúscula
name = name.capitalize()

.title = Todas as primeiras letras de cada palavra ficam maiúsculas
name = name.title()

name = input("What's your name? ")
name = name.strip().title()
ou
name = input("What's your name? ").strip().title()



.split("argumento que separa") = separa os argumentos, podendo criar novos parametros
first, last = name.split(" ")
print(f"Hello, {first}!")




---------------------------------------
name = input("What's your name? ").strip().title()

first, last = name.split(" ")

print(f"Hello, {first}!")



-------------------------------------

def -> cria uma função nova



def hello(to):
           ^-> faz a função aceitar parametros, nesse caso, apenas um parametro
    print("Hello,", to)
                     

name = input("What's your name? ")
hello(name)
        ^-> faz com que ele saiba qual a variavel utilizada no parametro

-----------------------------
def hello(to = "world"):
                  ^-> faz com que, se a função(hello, neste caso) for chama e não tiver input, ou se não for dado pelo programador, ela tenha um valor pré-definido, podendo, depois, ser alterada com outra linha de código contendo a váriavel
    print("Hello,", to)

hello()
name = input("What's your name? ")
hello(name)





--------------------------------
scope = quando uma variável só existe em uma 'def'
return = retorna o valor para a variavel
    ^-> def square(n):
        return n * n
        
https://cs50.harvard.edu/python/2022/psets/0/