# CALCULADORA

z = x + y
vai juntar e virar texto, ao invés de somar

int vai converter em número que posso fazer calculos
z = int(x) + int(y)

-------------------------------------------
x = int(input("Qual o x: "))
y = int(input("Qual o y: "))

print(x + y)

ou

x = input("Qual o x: ")
y = input("Qual o y: ")

print(int(x) + int(y))


---------------------------

float = aceita números decimais
round = arredonda números decimais 
^-> round(number[,ndigits])
                    ^-> se utilizar ', numero', ele diz qual digito após a casa decimal arredondar
                    ^->z = round(x / y, 2)
                    
exemplo = print(round(x + y))


print(f"{z:,}")
          ^-> :, faz com que os milhares sejam separados por ','


x = float(input("Qual o x: "))
y = float(input("Qual o y: "))

z = round(x + y)

print(f"{z:,}")



print(f"{z:.2f}") -> mostra apenas 2 numeros após a vírgula


------------------------


x = float(input("Qual o x: "))
y = float(input("Qual o y: "))

z = x / y

print(f"{z:.2f}")
